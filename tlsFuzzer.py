#!/usr/bin/python

import os
import sys
import socket
import string
from struct import *
from sFunctions import *
from constants import *
import tlslite
from tlslite.api import *
import base64
from Crypto.Cipher import AES
from array import *
import hashlib
from hashlib import *
import copy
import random
import hmac
import math

###############################################################################
#
# LibSSL --
#
# 			SSL Class for Fuzzer
#
###############################################################################

###############################################################################
#
# Handshake Messages (after removing Record Layer Header till CKEMessage) are:
#
# 					self.sslStruct['cHello']
#					self.sslStruct['sHello']
#					self.sslStruct['sCertificate']
#					self.sslStruct['sHelloDone']
#					self.sslStruct['ckeMessage']
#
###############################################################################


class LibTLS:
#
# Constructor
#
	def __init__(self, debugFlag = 0, config_obj_list = None, comm = None):
		self.sslStruct = {}
		self.comm = comm
		self.config_obj_list = config_obj_list
		self.clientHello = None
		self.debugFlag = debugFlag
		self.socket = None
		self.sslHandshake = None
		self.sslRecord = None
		self.opn = 0

###############################################################################
#
# TCPConnect --
#
# 			Establishes a TCP connection and returns 
#			the socket descriptor
#
# Results:
#			Establishes a TCP connection to a server:port 
#			and returns socket
#
# Side Effects:
#			None
###############################################################################
	def TCPConnect(self):
		self.socket = socket.socket(socket.AF_INET, 
					socket.SOCK_STREAM)
		self.socket.connect((self.comm.host, self.comm.port))


	#
	# get all keys of the hash
	#
	def get_keys(self):
		return self.config_hash.keys()

	#
	# get all values in the hash
	#
	def get_values(self):
		return self.config_hash.values()

	#
	# payload elements in the config_hash are of the form:
	#     
	#       <key> = <value> : <type>
        #
        #         where <key> is the name of the field
        #               <value> is the value of the field
        #                     -> <value> can only be a 
	#			 at this time
        #               <type> is the format in which
	#		      <value> should be packed
	#
	# NOTE: Keeping it as a hash to make it simple
	#

	#
	# get value corresponding to a key
	#
	def get_value(self, key):
		value = None
		for iter1 in self.config_obj_list:
			if iter1.key == key:
				try:
					value = iter1.value
					break					
				except:
					value = None
		return value

	#
	# get type corresponding to a key
	#
	def get_type(self, key):
		tp = None
		for iter1 in self.config_obj_list:
			if iter1.key == key:
				try:
					tp = iter1.tp
					break					
				except:
					tp = None
		return tp
	#
	# set value for a key
	#
	def set_value(self, key, value):
		for iter1 in self.config_obj_list:
			if iter1.key == key:
				iter1.value = value
				break

	#
	# set type for a key
	#
	def set_type(self, key, tp):
		for iter1 in self.config_obj_list:
			if iter1.key == key:
				iter1.tp = tp
				break
		

	#
	# get length of value of a key
	#
	def get_len(self, key):
		ln = None
		for iter1 in self.config_obj_list:
			if iter1.key == key:
				ln = len(iter1.value)
				break
		return ln

	def get_random_string(self, num_bytes):
		word = ''
		for i in range(num_bytes):
        		word += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
		return word

###############################################################################
#
# CreateClientHello --
#
# 			Function to create a SSL Client Hello packet
#
# Results:
#			1. Creates a customized SSL Client Hello packet
#
# Side Effects:
#			None
###############################################################################
	def CreateClientHello(self, cipher = None):
		if self.comm.config.get_value("client_hello_hs_cipher_suites") == "DECIDE":
	                if cipher != None:
        	                self.set_value("client_hello_hs_cipher_suites",
                	                cipher)
				self.set_type("client_hello_hs_cipher_suites", ">H")

	                        self.set_value("client_hello_hs_cipher_suites_len", 2)
				self.set_type("client_hello_hs_cipher_suites_len", ">H")
			else:
				self.set_value("client_hello_hs_cipher_suites", 
					DEFAULT_CH_CIPHER_SUITES)
				self.set_type("client_hello_hs_cipher_suites", ">H")

	                        self.set_value("client_hello_hs_cipher_suites_len", 2)
				self.set_type("client_hello_hs_cipher_suites_len", ">H")

			if self.comm.config.get_value("client_hello_hs_cipher_suites_len") == "DECIDE":
				if cipher != None:
	                                self.set_value("client_hello_hs_cipher_suites_len", 2)
					self.set_type("client_hello_hs_cipher_suites_len", ">H")
				else:
					self.set_value("client_hello_hs_cipher_suites_len",
						len(DEFAULT_CH_CIPHER_SUITES))
					self.set_type("client_hello_hs_cipher_suites_len", ">H")

		else:
			if self.comm.config.get_value("client_hello_hs_cipher_suites_len") == "DECIDE":
				setting = "%d:>H" % (len(self.get_value("client_hello_hs_cipher_suites")))
				self.set_value("client_hello_hs_cipher_suites_len", 
					len(self.get_value("client_hello_hs_cipher_suites")))
				self.set_type("client_hello_hs_cipher_suites_len", ">H")

		#
		# Handle client random
		#
		if self.comm.config.get_value("client_hello_hs_client_random") == "DECIDE":
			self.set_value("client_hello_hs_client_random", DEFAULT_CH_CLIENT_RANDOM)
			self.set_type("client_hello_hs_client_random", "S")

		self.sslStruct['cHelloRB'] = self.get_value("client_hello_hs_client_random")

		#
		# Handle compression methods
		#
		if self.comm.config.get_value("client_hello_hs_compression_methods") == "DECIDE":
			setting = pack('H', 1)
			self.set_value("client_hello_hs_compression_methods", setting)
			self.set_type("client_hello_hs_compression_methods", "H")
		
		#
		# Length of handshake part = 
		# 	Length of handshake ssl version (H) +
		#	Length of client random (32 bytes) +
		#	Length of client sid (B) +
		#	Length of cipher_suites_length (H) +
		#	Length of cipher_suites (variable) + 
		#	Length of compression_methods (variable)
		#
		if self.comm.config.get_value("client_hello_hs_length") == "DECIDE":
			self.client_hello_hs_length = calcsize('>HBH') + 32 + \
				int(self.get_value("client_hello_hs_cipher_suites_len")) + \
				2
			self.set_value("client_hello_hs_length",
				self.client_hello_hs_length)
			self.set_type("client_hello_hs_length", ">H")
		else:
			self.client_hello_hs_length = \
				self.get_value("client_hello_hs_length")

		self.set_value("client_hello_hs_length", self.client_hello_hs_length)
		self.set_type("client_hello_hs_length", ">H")

		if self.comm.config.get_value("client_hello_record_length") == "DECIDE":
			self.client_hello_record_length = self.client_hello_hs_length + \
				4
		else:
			self.client_hello_record_length = self.get_value("client_hello_record_length")

		self.set_value("client_hello_record_length", self.client_hello_record_length)
		self.set_type("client_hello_record_length", ">H")

		if self.sslRecord == None:
			self.sslRecord = ""
		if self.sslHandshake == None:
			self.sslHandshake = ""
		self.sslStruct['cHelloRB'] = self.get_value("client_hello_hs_client_random")

		for iter1 in self.config_obj_list:
                	if "client_hello_hs" in iter1.key:
	                        value = iter1.value
        	                tp = iter1.tp

        	                #
        	                # packed_value = pack(value) in the form of int
        	                #                       or if that fails, value
        	                #
	                        try:
					if "client_hello_hs_length" in iter1.key:
						packed_value = pack('>B', 0) + pack('>H', self.client_hello_hs_length)
					else:        
						packed_value = pack('%s' % (tp), int(value))
        	                except ValueError:
        	                        packed_value = value

        	                #
        	                # Add packed value
        	                #       
        	                self.sslHandshake = self.sslHandshake + str(packed_value)

		self.sslStruct['cHello'] = self.sslHandshake
		if (self.debugFlag == 1):	
			pBanner("Creating ClientHello")
			print "\nLength of ClientHello:" + \
			str(len(self.sslStruct['cHello']))

			HexStrDisplay(	"ClientHello Message Created", 
					Str2HexStr(self.sslStruct['cHello']))
			pBanner("Created ClientHello")

###############################################################################
#
# ReadServerHello --
#
# 			Function to read a ServerHello 
#			Message sent by SSL Server
#
# Results:
#			1. Reads ServerHello Message sent by server 
#			2. Interprets its details
#			3. Stores necessary values as part of sslStruct
#
# Side Effects:
#			None
###############################################################################
	def ReadServerHello(self):
		if self.debugFlag == 1:
			pBanner("Reading ServerHello")
		header = self.socket.recv(5)

		if len(header) == 0:
			self.opn = 1
			return 		
		shLen = HexStr2IntVal(header, 3, 4)

		if shLen == 2:
			self.opn = 1

		sHello = ""
		#
		# Added 
		#		
		if shLen > 500:
			header = self.socket.recv(4)
			shLen = HexStr2IntVal(header, 1, 3)
			sHello = header
		#

		self.sslStruct['shLen'] = shLen
		sHello = sHello + self.socket.recv(shLen)

		self.sslStruct['sHello'] = sHello
		self.sslStruct['sHelloRB'] = sHello[6:32+6]

		if (self.debugFlag == 1):		
			HexStrDisplay(	"ServerHello Message Received", 
					Str2HexStr(self.sslStruct['sHello']))
			HexStrDisplay(  "ServerHello Random Bytes",
					Str2HexStr(self.sslStruct['sHelloRB']))	
			pBanner("Read ServerHello")

###############################################################################
#
# ReadServerCertificate --
#
# 			Function to read a ServerCertificate Message 
#			sent by SSL Server
#
# Results:
#			1. Reads ServerCertificate Message sent by server 
#			2. Interprets its details
#			3. Stores necessary values as part of sslStruct
#
# Side Effects:
#			None
###############################################################################
	def ReadServerCertificate(self):
		if self.debugFlag == 1:
			pBanner("Reading ServerCertificate")
		
		header = self.socket.recv(1)
		packet_type = ord(header[0])
		packet_type_h = header[0]
		if packet_type == 22:
			header = self.socket.recv(4)
			if len(header) == 0:
				self.opn = 1
				return
			scLen = HexStr2IntVal(header, 2, 3)
			self.sslStruct['scLen'] = scLen
			sCertificate = self.socket.recv(scLen)
		else:
			header = self.socket.recv(3)
			if len(header) == 0:
				self.opn = 1
				return
			scLen = HexStr2IntVal(header, 1, 2)
			self.sslStruct['scLen'] = scLen

			packet_extra = packet_type_h + header
			sCertificate = self.socket.recv(scLen)
			sCertificate = packet_extra + sCertificate
			
		self.sslStruct['sCertificate'] = sCertificate[10:]
		self.sslStruct['sCertificateCF'] = sCertificate

		if (self.debugFlag == 1):
			HexStrDisplay("Server Certificate", 
				Str2HexStr(self.sslStruct['sCertificate']))
			HexStrDisplay("Server Certificate CF", 
				Str2HexStr(self.sslStruct['sCertificateCF']))

		

		fobject = open("./files/servercrt.pem", 'w')
		fobject.write("-----BEGIN CERTIFICATE-----\n")
		output = base64.b64encode(self.sslStruct['sCertificate'])

		count = 0
		final_output = ""
		for iter1 in output:
			final_output += iter1
			count += 1
			if count == 64:
				count = 0
				final_output += "\r\n"

		fobject.write(final_output)
		fobject.write("\n-----END CERTIFICATE-----\n")
		fobject.close()

		sCert = open("./files/servercrt.pem").read()
		x509 = X509()
		cert = x509.parse(sCert)

		x509cc = X509CertChain([x509])
		if self.debugFlag == 1:
			HexStrDisplay("Fingerprint",Str2HexStr(x509.getFingerprint()))
			print "\nNumber of Certificates: " + str(x509cc.getNumCerts())
			pBanner("Read ServerCertificate")

###############################################################################
#
# read_server_key_exchange --
#
# 			Function to read a Server Key Exchange Message 
#			sent by SSL Server
#
# Results:
#			1. Reads ServerCertificate Message sent by server 
#			2. Interprets its details
#			3. Stores necessary values as part of sslStruct
#
# Side Effects:
#			None
###############################################################################
	def ReadServerKeyExchange(self):
		if self.debugFlag == 1:
			pBanner("Reading Server Key Exchange")
		header = self.socket.recv(5)
		if len(header) == 0:
			self.opn = 1
			return 0
		scLen = HexStr2IntVal(header, 3, 4)
		self.sslStruct['skeLen'] = scLen
		ske = self.socket.recv(scLen)
		self.sslStruct['ske'] = ske

		if self.debugFlag == 1:
			HexStrDisplay("Server Key Exchange",Str2HexStr(ske))
			pBanner("Read Server Key Exchange")

###############################################################################
#
# ReadServerHelloDone --
#
# 			Function to read a ServerHelloDone 
#			Message sent by SSL Server
#
# Results:
#			1. Reads ServerHelloDone Message sent by server 
#			2. Interprets its details
#			3. Stores necessary values as part of sslStruct
#
# Side Effects:
#			None
###############################################################################
	def ReadServerHelloDone(self):
		if self.debugFlag == 1:
			pBanner("Reading ServerHelloDone")
		
		header = self.socket.recv(1)
		packet_type = ord(header[0])
		packet_type_h = header[0]

		if packet_type == 22:
			header = self.socket.recv(4)
			if len(header) == 0:
				self.opn = 1
				return
			scLen = HexStr2IntVal(header, 2, 3)
		else:
			header = self.socket.recv(3)
			if len(header) == 0:
				self.opn = 1
				return
			scLen = HexStr2IntVal(header, 1, 2)
	
		if scLen > 0:
			sHelloDone = self.socket.recv(scLen)
			self.sslStruct['sHelloDone'] = sHelloDone
		else:
			self.sslStruct['sHelloDone'] = packet_type_h + \
				header

		if (self.debugFlag == 1):
			HexStrDisplay("Server HelloDone", 
				Str2HexStr(self.sslStruct['sHelloDone']))
			pBanner("Read ServerHelloDone")

###############################################################################
#
# SendCT --
#
# 			Function to send a cleartext ssl handshake
#			message
#
# Results:
#			1. SSL cleartext record layer header is added
#			2. clear text handshake message is sent
#
# Side Effects:
#			None
###############################################################################

	def SendCTPacket(self):
		recMsg = 	tlsRecHeaderDeafult  + \
				Pack2Bytes(len(self.sslHandshake))
	
		self.sslRecord = recMsg + self.sslHandshake
		
		if self.debugFlag == 1:
			pBanner("Sending CT Packet")
			print "\nLength of HS Message: ", str(len(self.sslHandshake))
			print "\nLength of Total Message: ", str(len(self.sslRecord))
			HexStrDisplay("HS Message CT:", Str2HexStr(self.sslHandshake))
			HexStrDisplay("Total Message CT:", Str2HexStr(self.sslRecord))

		try:
			self.socket.send(self.sslRecord)
		except:
			self.opn = 1

		if self.debugFlag == 1:
			pBanner("Sent CT Packet")

##############################################################################
#
# SendSSLPacket --
#
# 			Function to send an SSL handshake packet after adding
#			record layer headers
#
# Results:
#			1. Takes SSL Handshake message as input
#			2. Adds SSL record layer headers to it
#			3. Sends the packet to Server
#
# Side Effects:
#			None
###############################################################################
	def SendSSLPacket(self, hsMsg, seq, renegotiate):
			if self.debugFlag == 1:
				pBanner("Sending SSL Packet")
			import socket
			import struct
			rec = hsMsg
			recLen = len(hsMsg)
			if self.debugFlag == 1:
				HexStrDisplay("Record Length", Str2HexStr(Pack2Bytes(recLen)))
				HexStrDisplay("Record", Str2HexStr(rec))
			seqNum = seq
			seqNumUnsignedLongLong = pack('>Q', seqNum)
			iHash = pack('B', 22)
			iHash1 = pack('>H', recLen)

			m = hmac.new(self.sslStruct['wMacPtr'], digestmod=sha1)
			m.update("\x00\x00\x00\x00\x00\x00\x00\x00")
			m.update("\x16")
			m.update("\x03")
			m.update("\x01")
			m.update(iHash1)
			m.update(rec)
			m = m.digest()

			if self.debugFlag == 1:
				HexStrDisplay("Final MAC", Str2HexStr(m))
	
			self.sslStruct['recordPlusMAC'] = rec + m
			currentLength = len(rec + m) + 1
			blockLength = 16
			pad_len = blockLength -(currentLength % blockLength)
			if self.debugFlag == 1:
				print "\nPadding Length: " + str(pad_len)
			padding = ''
			for iter in range(0, pad_len + 1):
				padding = padding + struct.pack('B', pad_len)

			if self.debugFlag == 1:
				HexStrDisplay("Padding", Str2HexStr(padding))
			
			self.sslStruct['recordPlusMAC'] = rec + m + padding
			if self.debugFlag == 1:
				HexStrDisplay("Record + MAC", 
				      Str2HexStr(self.sslStruct['recordPlusMAC']))
	
			if renegotiate == 1:
				from Crypto.Cipher import AES
				global hswr
				hswr = AES.new( self.sslStruct['wKeyPtr'], AES.MODE_CBC, self.sslStruct['wIVPtr'] )
				encryptedData = hswr.encrypt(self.sslStruct['recordPlusMAC'])

			if renegotiate == 0:
				from Crypto.Cipher import AES
				global hswor
				hswor = AES.new( self.sslStruct['wKeyPtr'], AES.MODE_CBC, self.sslStruct['wIVPtr'] )
				encryptedData = hswor.encrypt(self.sslStruct['recordPlusMAC'])


			if self.debugFlag == 1:
				HexStrDisplay("Encrypted Record + MAC", 
					Str2HexStr(encryptedData))
	
			packLen = len(encryptedData)

			self.sslStruct['encryptedRecordPlusMAC'] = tlsRecHeaderDeafult + \
					Pack2Bytes(packLen) + encryptedData

			if self.debugFlag == 1:
				HexStrDisplay("Packet Sent", 
					Str2HexStr(self.sslStruct['encryptedRecordPlusMAC']))
		
			self.socket.send(
				self.sslStruct['encryptedRecordPlusMAC'])
			self.sslStruct['wIVPtr'] = encryptedData[len(encryptedData) - 16 :len(encryptedData)]

			if self.debugFlag == 1:
				pBanner("Sent SSL Packet")

##############################################################################
#
# SendRecordPacket --
#
# 			Function to send an SSL Application Data after adding
#			record layer headers
#
# Results:
#			1. Takes SSL record message as input
#			2. Adds SSL record layer headers to it
#			3. Sends the packet to Server
#
# Side Effects:
#			None
###############################################################################
	def SendRecordPacket(self, recMsg, seq):
			if self.debugFlag == 1:
				pBanner("Sending SSL Record Packet")
			import struct
			import socket
			rec = recMsg
			recLen = len(recMsg)
			if self.debugFlag == 1:
				HexStrDisplay("Record Length", Str2HexStr(Pack2Bytes(recLen)))
				HexStrDisplay("Record", Str2HexStr(rec))

			iHash1 = pack('>H', recLen)

			m = hmac.new(self.sslStruct['wMacPtr'], digestmod=sha1)
			m.update("\x00\x00\x00\x00\x00\x00\x00\x01")
			m.update("\x17")
			m.update("\x03")
			m.update("\x01")
			m.update(iHash1)
			m.update(rec)
			m = m.digest()

			if self.debugFlag == 1:	
				HexStrDisplay("Final MAC", Str2HexStr(m))
	

			currentLength = len(rec + m) + 1
			blockLength = 16
			pad_len = blockLength -(currentLength % blockLength)
			print "\r\nCurrentLength mod BlockLength = %d\r\n" % (currentLength % blockLength)
			if self.debugFlag == 1:
				print "\nPadding Length: " + str(pad_len)
			padding = ''
			for iter in range(0, pad_len + 1):
				padding = padding + struct.pack('B', pad_len)

			self.sslStruct['recordPlusMAC'] = rec + m + padding

			if self.debugFlag == 1:
				HexStrDisplay("Record + MAC", 
				      Str2HexStr(self.sslStruct['recordPlusMAC']))

			from Crypto.Cipher import AES
			global ciph
			ciph = AES.new( self.sslStruct['wKeyPtr'], AES.MODE_CBC, self.sslStruct['wIVPtr'] )
			encryptedData = ciph.encrypt(self.sslStruct['recordPlusMAC'])
	
			if self.debugFlag == 1:			
				HexStrDisplay("Encrypted Record + MAC", 
					Str2HexStr(encryptedData))
	
			packLen = len(encryptedData)
			self.sslStruct['encryptedRecordPlusMAC'] = tlsAppHeaderDefault + \
					Pack2Bytes(packLen) + encryptedData

			if self.debugFlag == 1:
				HexStrDisplay("Packet Sent", 
					Str2HexStr(self.sslStruct['encryptedRecordPlusMAC']))
		
			self.socket.send(
				self.sslStruct['encryptedRecordPlusMAC'])

			self.sslStruct['wIVPtr'] = encryptedData[len(encryptedData) - 16 :len(encryptedData)]
			pBanner("Sent SSL Record Packet")

##############################################################################
#
# ReadCTPacket --
#
# 			Function to read cleartext response from server
#
# Results:
#			1. Reads cleartext response from server
#			3. Stores necessary values as part of sslStruct
#
# Side Effects:
#			None
###############################################################################
	def ReadCTPacket(self):
			if self.debugFlag == 1:
				pBanner("Reading CT Packet")
			socket = self.socket
			header = self.socket.recv(5)
			recLen = HexStr2IntVal(header, 3, 4)
			data = self.socket.recv(recLen)
			if self.debugFlag == 1:
				print str(data)
				pBanner("Read CT Packet")			

##############################################################################
#
# ReadSSLPacket --
#
# 			Function to read response from server
#
# Results:
#			1. Reads response from server
#			3. Stores necessary values as part of sslStruct
#
# Side Effects:
#			None
###############################################################################
	def ReadSSLPacket(self):
			if self.debugFlag == 1:
				pBanner("Reading SSL Packet")
			header = self.socket.recv(5)
			recLen = HexStr2IntVal(header, 3, 4)

			try:
				data = self.socket.recv(recLen)
			except:
				self.opn = 1
				return

			if self.debugFlag == 1:
				HexStrDisplay("Encrypted Data", Str2HexStr(data))
			from Crypto.Cipher import AES
			global i
			i = AES.new( self.sslStruct['rKeyPtr'], AES.MODE_CBC, self.sslStruct['rIVPtr'] )
			decryptedCF = i.decrypt(data)

			self.sslStruct['rIVPtr'] = data[recLen - 16: recLen]
			self.decryptedData = decryptedCF

			if self.debugFlag == 1:
				print "\nPlainText Data:\n" + decryptedCF + "\n"
				HexStrDisplay("DecryptedData", Str2HexStr(decryptedCF))
				pBanner("Read SSL Packet")			

##############################################################################
#
# ReadSF --
#
# 			Function to read ServerFinished Message from server
#
# Results:
#			1. Reads ChangeCipherSpec and ServerFinished Message from server
#			3. Stores necessary values as part of sslStruct
#
# Side Effects:
#			None
###############################################################################
	def ReadSF(self):
			if self.debugFlag == 1:
				pBanner("Reading ServerFinished from server")
			socket = self.socket
			header = self.socket.recv(5)
			CFLen = HexStr2IntVal(header, 3, 4)
			if CFLen == 1:
				if self.debugFlag == 1:
					print "\nINFO: Received Server Change Cipher Spec\nLen = " + str(CFLen)
				cssSer = self.socket.recv(1)
			header = self.socket.recv(5)
			CFLen = HexStr2IntVal(header, 3, 4)
			if self.debugFlag == 1:
				print "\nINFO: Received ServerFinished Message of Length: " + str(CFLen)
			CFMessage = self.socket.recv(CFLen)
			if (CFMessage):
				if self.debugFlag == 1:
					HexStrDisplay("\nINFO: Finished Read from Server",
						Str2HexStr(CFMessage))

			from Crypto.Cipher import AES
			global f
			f = AES.new( self.sslStruct['rKeyPtr'], AES.MODE_CBC, self.sslStruct['rIVPtr'] )
			decryptedCF = f.decrypt(CFMessage)

			self.sslStruct['rIVPtr'] = CFMessage[48:64]
			if self.debugFlag == 1:
				HexStrDisplay("\nINFO: Decrypted Finished Message from Server", 
					Str2HexStr(decryptedCF[0:40]))
				pBanner("Read ServerFinished from server")	

	def P_hash(self, hashModule, secret, seed, length):
	    	bytes = bytearray(length)
	    	A = seed
	    	index = 0
	    	while 1:
			A = hmac.HMAC(secret, A, hashModule).digest()
			output = hmac.HMAC(secret, A+seed, hashModule).digest()
			for c in output:
		    		if index >= length:
		        		return bytes
		    		bytes[index] = c
		    		index += 1
	    

	def PRF(self, secret, label, seed, length):
	    	#Split the secret into left and right halves
	    	# which may share a byte if len is odd
	    	S1 = secret[ : int(math.ceil(len(secret)/2.0))]
	    	S2 = secret[ int(math.floor(len(secret)/2.0)) : ]

	    	#Run the left half through P_MD5 and the right half through P_SHA1
		seed = label + seed
	    	p_md5 = self.P_hash(md5, S1, seed, length)
	    	p_sha1 = self.P_hash(sha1, S2, seed, length)

	    	#XOR the output values and return the result
	    	for x in range(length):
			p_md5[x] ^= p_sha1[x]

	    	return p_md5


##############################################################################
#
# CreateClientKeyExchange --
#
# 			Function to create a ClientKeyExchange message
#
# Results:
#			1. Creates ClientKeyExchange Message
#			3. Stores necessary values as part of sslStruct
#
# Side Effects:
#			None
###############################################################################
	def CreateClientKeyExchange(self):
		if self.debugFlag == 1:
			pBanner("Creating ClientKeyExchange")


		#
		# TLS encryption
		#
		sCert = open("./files/servercrt.pem").read()
		x509 = X509()
		cert = x509.parse(sCert)

		x509cc = X509CertChain([x509])
		ckeArray = array ( 'B', tlsCKEPMKey)
		encData = cert.publicKey.encrypt(ckeArray)
		encDataStr_tls = encData.tostring()

		self.sslStruct['encryptedPMKey'] = encDataStr_tls
		self.sslStruct['encryptedPMKey_len'] = len(self.sslStruct['encryptedPMKey'])

		self.sslStruct['ckeMessage'] = 	ckeMsgHdr + \
			Pack3Bytes(self.sslStruct['encryptedPMKey_len'] + 2) + \
			Pack2Bytes(self.sslStruct['encryptedPMKey_len']) + \
			self.sslStruct['encryptedPMKey']

		HexStrDisplay("Client Key Exchange", Str2HexStr(self.sslStruct['ckeMessage']))

		if (self.debugFlag == 1):
			HexStrDisplay("Client KeyExchange Message", 
				Str2HexStr(self.sslStruct['ckeMessage']))
			HexStrDisplay("Client Encrypted Pre Master Key", 
				Str2HexStr(self.sslStruct['encryptedPMKey']))
			HexStrDisplay("Client ChangeCipherSpec Message", 
				Str2HexStr(cssPkt))			
		self.encrypted = 0
		self.sslHandshake = self.sslStruct['ckeMessage']	
		if self.debugFlag == 1:
			pBanner("Created ClientKeyExchange")

##############################################################################
#
# CreateMasterSecret --
#
# 			Function to create a MasterSecret
#
# Results:
#			1. Creates MasterSecret
#			3. Stores necessary values as part of sslStruct
#
# Side Effects:
#			None
###############################################################################

#
# master_secret = MD5(premaster_secret + SHA('A' + client_random + 
#		  server_random + premaster_secret)) +
#		  MD5(premaster_secret + SHA('BB' + client_random + 
#		  server_random + premaster_secret)) +
#		  MD5(premaster_secret + SHA('CCC' + client_random + 
#		  server_random + premaster_secret))
#
#

	def CreateMasterSecret(self):
		if self.debugFlag == 1:
			pBanner("Creating MasterSecret")
		

			HexStrDisplay("ClientRandom:", 
				Str2HexStr(self.sslStruct['cHelloRB']))
			HexStrDisplay("ServerRandom:", 
				Str2HexStr(self.sslStruct['sHelloRB']))
			HexStrDisplay("ckePMKey:", Str2HexStr(ckePMKey))

		self.sslStruct['masterSecret'] = self.PRF(tlsCKEPMKey,
					"master secret", 
					self.sslStruct['cHelloRB'] + \
					self.sslStruct['sHelloRB'],
					48)

		master_secret_str = ""
		for ch in self.sslStruct['masterSecret']:
			master_secret_str += chr(ch)

		self.sslStruct['masterSecret'] = master_secret_str
		if self.debugFlag == 1:
			HexStrDisplay("MasterSecret", 
				Str2HexStr(self.sslStruct['masterSecret']))
			pBanner("Created MasterSecret")


##############################################################################
#
# CreateFinishedHash --
#
# 			Function to create a ClientFinished MD5 and SHA Hashes
#
# Results:
#			1. Creates ClientFinished MD5 and SHA Hashes
#			3. Stores necessary values as part of sslStruct
#
# Side Effects:
#			None
###############################################################################

#
#   ClientFinishedMessage = md5_hash + sha1_Hash
#
#    			    md5_hash = MD5(master_secret + pad2md5 + 
#			    MD5(handshake_messages + Sender + master_secret + 
#			    pad1md5));
#			
#			    sha1_hash =  SHA(master_secret + pad2sha +
#			    SHA(handshake_messages + Sender + master_secret + 
#			    pad1sha));
#
	def CreateFinishedHash(self):
		if self.debugFlag == 1:
			pBanner("Creating Finished Hash")
	

			HexStrDisplay("ClientHello", Str2HexStr(self.sslStruct['cHello']))
			HexStrDisplay("ServerHello", Str2HexStr(self.sslStruct['sHello']))
			HexStrDisplay("Server Certificate", 
				Str2HexStr(self.sslStruct['sCertificateCF']))
			HexStrDisplay("Server Hello Done", 
				Str2HexStr(self.sslStruct['sHelloDone']))
			HexStrDisplay("Client Key Exchange", 
				Str2HexStr(self.sslStruct['ckeMessage']))
			HexStrDisplay("Master Secret", 
				Str2HexStr(self.sslStruct['masterSecret']))

		

		m1 = md5()
		m1.update(self.sslStruct['cHello'])
		m1.update(self.sslStruct['sHello'])
		m1.update(self.sslStruct['sCertificateCF'])
		m1.update(self.sslStruct['sHelloDone'])
		m1.update(self.sslStruct['ckeMessage'])
		md5Hash = m1.digest()
	

		s1 = sha1()
		s1.update(self.sslStruct['cHello'])
		s1.update(self.sslStruct['sHello'])
		s1.update(self.sslStruct['sCertificateCF'])
		s1.update(self.sslStruct['sHelloDone'])
		s1.update(self.sslStruct['ckeMessage'])
		shaHash = s1.digest()
		

		cFinished = self.PRF(self.sslStruct['masterSecret'], 
			'client finished',
			md5Hash + shaHash, 12)

		cFinished_str = str(cFinished)
		cfLen = len(cFinished_str)
		cfLen = Pack3Bytes(cfLen)

		self.sslStruct['cFinished'] = "\x14" + cfLen + \
					cFinished_str


		if self.debugFlag == 1:
			HexStrDisplay("MD5 Hash", Str2HexStr(md5Hash))
			HexStrDisplay("SHA Hash", Str2HexStr(shaHash))

			HexStrDisplay("ClientFinished Message", 
				Str2HexStr(self.sslStruct['cFinished']))

			pBanner("Created Finished Hash")

##############################################################################
#
# CreateKeyBlock --
#
# 			Function to create a Key Block
#
# Results:
#			1. Creates a Key Block
#			3. Stores necessary values as part of sslStruct
#
# Side Effects:
#			None
###############################################################################

# 
# key_block =
#	  MD5(master_secret + SHA('A' + master_secret + ServerHello.random +
#		  ClientHello.random)) +
#	  MD5(master_secret + SHA('BB' + master_secret + ServerHello.random +
#		  ClientHello.random)) +
#	  MD5(master_secret + SHA('CCC' + master_secret + ServerHello.random +
#		  ClientHello.random)) + [...];
#

	def CreateKeyBlock(self):
		if self.debugFlag == 1:
			pBanner("Creating Key Block")
		

		self.sslStruct['digLen'] = 16
		self.sslStruct['keyBits'] = 128
		self.sslStruct['blockBits'] = 0
		self.sslStruct['ivSize'] = 0
		self.sslStruct['macSize'] = self.sslStruct['digLen']
		self.sslStruct['keySize'] = self.sslStruct['keyBits'] / 8
		self.sslStruct['writeSeq'] = 0
		self.sslStruct['readSeq'] = 0
		self.sslStruct['reqKeyLen'] = 	2 * self.sslStruct['macSize'] + \
						2 * self.sslStruct['keySize'] + \
						2 * self.sslStruct['ivSize']
		self.sslStruct['keyIter'] = 9
		self.sslStruct['keyBlock'] = ""


		seed = self.sslStruct['sHelloRB'] + self.sslStruct['cHelloRB']
		self.sslStruct['keyBlock'] = self.PRF(self.sslStruct['masterSecret'], 'key expansion', seed, 104)


		keyBlock_str = ""
		for ch in self.sslStruct['keyBlock']:
			keyBlock_str += chr(ch)

		self.sslStruct['keyBlock'] = keyBlock_str

	
		self.sslStruct['wMacPtr'] = self.sslStruct['keyBlock'][0:20]
		self.sslStruct['rMacPtr'] = self.sslStruct['keyBlock'][20:40]
		self.sslStruct['wKeyPtr'] = self.sslStruct['keyBlock'][40:56]
		self.sslStruct['rKeyPtr'] = self.sslStruct['keyBlock'][56:72]
		self.sslStruct['wIVPtr'] = self.sslStruct['keyBlock'][72:88]
		self.sslStruct['rIVPtr'] = self.sslStruct['keyBlock'][88:104]

		if self.debugFlag == 1:
			HexStrDisplay("Key Block", Str2HexStr(self.sslStruct['keyBlock']))
			HexStrDisplay("wMacPtr", Str2HexStr(self.sslStruct['wMacPtr']))
			HexStrDisplay("rMacPtr", Str2HexStr(self.sslStruct['rMacPtr']))
			HexStrDisplay("wKeyPtr", Str2HexStr(self.sslStruct['wKeyPtr']))
			HexStrDisplay("rKeyPtr", Str2HexStr(self.sslStruct['rKeyPtr']))
			HexStrDisplay("wIVPtr", Str2HexStr(self.sslStruct['wIVPtr']))
			HexStrDisplay("rIVPtr", Str2HexStr(self.sslStruct['rIVPtr']))

			pBanner("Created Key Block")
