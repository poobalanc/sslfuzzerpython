# Introduction #

The script makes it possible to create various types of SSL packets and send it to server

As of now, only normal communication has been tested

# Details #

The following would be the output of communicating with a public SSL Server:

```

root@family:/home/family/sslfuzzerpython-read-only/AES-Encryption# python fuzzSSL.py sourceforge.net 443

chLength:
00  00  29  
################INFO: Creating ClientHello ##############


Length of ClientHello:45

ClientHello Message Created:
01  00  00  29  03  00  44  44  - 44  44  66  66  66  66  66  66  
66  66  66  66  66  66  66  66  - 66  66  66  66  66  66  66  66  
66  66  66  66  66  66  00  00  - 02  00  35  01  00  
################INFO: Created ClientHello ##############


################INFO: Sending CT Packet ##############


Length of HS Message:  45

Length of Total Message:  50

HS Message CT::
01  00  00  29  03  00  44  44  - 44  44  66  66  66  66  66  66  
66  66  66  66  66  66  66  66  - 66  66  66  66  66  66  66  66  
66  66  66  66  66  66  00  00  - 02  00  35  01  00  
Total Message CT::
16  03  00  00  2d  01  00  00  - 29  03  00  44  44  44  44  66  
66  66  66  66  66  66  66  66  - 66  66  66  66  66  66  66  66  
66  66  66  66  66  66  66  66  - 66  66  66  00  00  02  00  35  
01  00  
################INFO: Sent CT Packet ##############


################INFO: Reading ServerHello ##############


ServerHello Message Received:
02  00  00  46  03  00  15  d8  - 81  9d  f4  5e  48  3b  5e  5d  
93  20  4b  78  ac  72  76  90  - 23  a4  ad  79  c1  35  ca  80  
76  85  06  ca  86  39  20  e3  - 5a  11  e2  96  c4  40  e9  0e  
50  4e  bc  ee  9e  a8  3d  cc  - 03  57  b2  b3  ac  91  f1  76  
d0  bd  9f  e8  11  3d  a6  00  - 35  00  
ServerHello Random Bytes:
15  d8  81  9d  f4  5e  48  3b  - 5e  5d  93  20  4b  78  ac  72  
76  90  23  a4  ad  79  c1  35  - ca  80  76  85  06  ca  86  39  

################INFO: Read ServerHello ##############


################INFO: Reading ServerCertificate ##############


Server Certificate:
30  82  03  77  30  82  02  e0  - a0  03  02  01  02  02  03  13  
87  19  30  0d  06  09  2a  86  - 48  86  f7  0d  01  01  05  05  
00  30  4e  31  0b  30  09  06  - 03  55  04  06  13  02  55  53  
31  10  30  0e  06  03  55  04  - 0a  13  07  45  71  75  69  66  
61  78  31  2d  30  2b  06  03  - 55  04  0b  13  24  45  71  75  
69  66  61  78  20  53  65  63  - 75  72  65  20  43  65  72  74  
69  66  69  63  61  74  65  20  - 41  75  74  68  6f  72  69  74  
79  30  1e  17  0d  31  30  30  - 36  32  32  30  37  34  30  35  
39  5a  17  0d  31  31  30  39  - 32  33  31  39  32  34  32  35  
5a  30  81  e5  31  29  30  27  - 06  03  55  04  05  13  20  75  
58  36  78  6f  35  75  6e  6e  - 63  67  4d  32  72  75  45  56  
48  59  69  76  46  4b  38  50  - 58  4b  6e  2d  73  6b  50  31  
0b  30  09  06  03  55  04  06  - 13  02  55  53  31  18  30  16  
06  03  55  04  0a  13  0f  73  - 6f  75  72  63  65  66  6f  72  
67  65  2e  6e  65  74  31  13  - 30  11  06  03  55  04  0b  13  
0a  33  37  35  34  35  30  38  - 30  35  36  31  31  30  2f  06  
03  55  04  0b  13  28  53  65  - 65  20  77  77  77  2e  67  65  
6f  74  72  75  73  74  2e  63  - 6f  6d  2f  72  65  73  6f  75  
72  63  65  73  2f  63  70  73  - 20  28  63  29  31  30  31  2f  
30  2d  06  03  55  04  0b  13  - 26  44  6f  6d  61  69  6e  20  
43  6f  6e  74  72  6f  6c  20  - 56  61  6c  69  64  61  74  65  
64  20  2d  20  51  75  69  63  - 6b  53  53  4c  28  52  29  31  
18  30  16  06  03  55  04  03  - 13  0f  73  6f  75  72  63  65  
66  6f  72  67  65  2e  6e  65  - 74  30  81  9f  30  0d  06  09  
2a  86  48  86  f7  0d  01  01  - 01  05  00  03  81  8d  00  30  
81  89  02  81  81  00  da  38  - 4a  6b  65  29  33  be  05  4b  
57  b3  bc  d4  0e  b0  c1  41  - f4  c3  a6  70  3c  ee  ca  df  
30  03  ad  b1  0b  5d  75  56  - 21  4d  7b  58  64  cb  72  e8  
5b  09  3a  21  17  8e  5d  fa  - aa  29  09  42  db  13  45  30  
63  e5  64  da  6b  7e  d9  d5  - de  f7  bb  75  02  09  c2  9c  
ed  4e  7d  8a  83  d2  a7  01  - 8c  09  23  ab  2c  48  67  0a  
82  68  ab  e9  1f  f2  3a  fa  - 18  b2  5e  ba  cc  73  fc  7f  
c0  d3  cb  f8  e4  2f  bf  c6  - 1c  b7  2f  82  db  33  ba  83  
09  31  be  16  c2  a3  02  03  - 01  00  01  a3  81  ca  30  81  
c7  30  1f  06  03  55  1d  23  - 04  18  30  16  80  14  48  e6  
68  f9  2b  d2  b2  95  d7  47  - d8  23  20  10  4f  33  98  90  
9f  d4  30  0e  06  03  55  1d  - 0f  01  01  ff  04  04  03  02  
04  f0  30  1d  06  03  55  1d  - 25  04  16  30  14  06  08  2b  
06  01  05  05  07  03  01  06  - 08  2b  06  01  05  05  07  03  
02  30  1a  06  03  55  1d  11  - 04  13  30  11  82  0f  73  6f  
75  72  63  65  66  6f  72  67  - 65  2e  6e  65  74  30  3a  06  
03  55  1d  1f  04  33  30  31  - 30  2f  a0  2d  a0  2b  86  29  
68  74  74  70  3a  2f  2f  63  - 72  6c  2e  67  65  6f  74  72  
75  73  74  2e  63  6f  6d  2f  - 63  72  6c  73  2f  73  65  63  
75  72  65  63  61  2e  63  72  - 6c  30  1d  06  03  55  1d  0e  
04  16  04  14  e7  e3  00  04  - 63  28  23  3c  82  64  5b  6c  
fa  f9  80  4d  ba  af  ef  4e  - 30  0d  06  09  2a  86  48  86  
f7  0d  01  01  05  05  00  03  - 81  81  00  61  68  b4  ac  83  
6e  4e  b6  cc  7c  5b  b0  a2  - ea  d5  a1  f2  d6  a1  08  0e  
1b  dc  f8  3a  7a  d4  fe  c0  - 2d  0e  e2  12  f8  eb  37  d3  
19  6b  c0  5e  47  cf  29  98  - 1b  0a  b7  97  1f  91  3e  3d  
71  4f  95  c8  2d  a4  97  b6  - 5f  d7  a9  97  b9  73  4a  c9  
68  ee  c0  a3  b4  3e  fd  2d  - 59  9b  ba  31  77  77  b5  17  
81  c5  ce  ec  63  30  16  9f  - 75  68  b2  cb  f4  83  d0  75  
51  64  8f  09  d9  a6  2b  9d  - f7  dd  af  0d  73  15  e2  9e  
df  9b  9c  8e  06  19  39  ff  - 7f  c2  b9  
Fingerprint:
34  36  31  63  64  31  65  66  - 36  65  36  39  31  66  38  36  
31  39  64  34  35  32  32  38  - 35  64  63  30  31  62  34  38  
34  63  30  35  39  38  37  61  - 
Number of Certificates: 1

################INFO: Read ServerCertificate ##############


################INFO: Reading ServerHelloDone ##############


Server HelloDone:
0e  00  00  00  
################INFO: Read ServerHelloDone ##############


################INFO: Creating ClientKeyExchange ##############


Client KeyExchange Message:
10  00  00  80  56  f6  6c  60  - e8  91  6d  58  0b  54  04  32  
db  9a  dc  3c  b7  fe  a6  11  - 92  9e  d1  f4  73  d2  a2  d8  
c4  bf  c2  6a  23  6d  8b  06  - 2f  ae  96  7e  7c  6e  a9  33  
29  61  92  50  dd  24  e6  2c  - 01  94  4d  61  a7  cb  34  7d  
f4  42  08  a6  cc  fc  d9  ca  - 43  e2  c2  21  4e  6b  7e  6b  
32  e4  11  8b  99  05  fd  31  - 63  18  49  54  67  9d  d0  1f  
92  b0  91  3d  d1  af  d8  7c  - ed  d0  21  94  89  70  bc  78  
33  cd  8d  0c  32  15  e2  29  - bc  59  69  98  6b  c2  a3  ab  
80  49  57  a9  
Client Encrypted Pre Master Key:
56  f6  6c  60  e8  91  6d  58  - 0b  54  04  32  db  9a  dc  3c  
b7  fe  a6  11  92  9e  d1  f4  - 73  d2  a2  d8  c4  bf  c2  6a  
23  6d  8b  06  2f  ae  96  7e  - 7c  6e  a9  33  29  61  92  50  
dd  24  e6  2c  01  94  4d  61  - a7  cb  34  7d  f4  42  08  a6  
cc  fc  d9  ca  43  e2  c2  21  - 4e  6b  7e  6b  32  e4  11  8b  
99  05  fd  31  63  18  49  54  - 67  9d  d0  1f  92  b0  91  3d  
d1  af  d8  7c  ed  d0  21  94  - 89  70  bc  78  33  cd  8d  0c  
32  15  e2  29  bc  59  69  98  - 6b  c2  a3  ab  80  49  57  a9  

Client ChangeCipherSpec Message:
14  03  00  00  01  01  
################INFO: Created ClientKeyExchange ##############


################INFO: Sending CT Packet ##############


Length of HS Message:  132

Length of Total Message:  137

HS Message CT::
10  00  00  80  56  f6  6c  60  - e8  91  6d  58  0b  54  04  32  
db  9a  dc  3c  b7  fe  a6  11  - 92  9e  d1  f4  73  d2  a2  d8  
c4  bf  c2  6a  23  6d  8b  06  - 2f  ae  96  7e  7c  6e  a9  33  
29  61  92  50  dd  24  e6  2c  - 01  94  4d  61  a7  cb  34  7d  
f4  42  08  a6  cc  fc  d9  ca  - 43  e2  c2  21  4e  6b  7e  6b  
32  e4  11  8b  99  05  fd  31  - 63  18  49  54  67  9d  d0  1f  
92  b0  91  3d  d1  af  d8  7c  - ed  d0  21  94  89  70  bc  78  
33  cd  8d  0c  32  15  e2  29  - bc  59  69  98  6b  c2  a3  ab  
80  49  57  a9  
Total Message CT::
16  03  00  00  84  10  00  00  - 80  56  f6  6c  60  e8  91  6d  
58  0b  54  04  32  db  9a  dc  - 3c  b7  fe  a6  11  92  9e  d1  
f4  73  d2  a2  d8  c4  bf  c2  - 6a  23  6d  8b  06  2f  ae  96  
7e  7c  6e  a9  33  29  61  92  - 50  dd  24  e6  2c  01  94  4d  
61  a7  cb  34  7d  f4  42  08  - a6  cc  fc  d9  ca  43  e2  c2  
21  4e  6b  7e  6b  32  e4  11  - 8b  99  05  fd  31  63  18  49  
54  67  9d  d0  1f  92  b0  91  - 3d  d1  af  d8  7c  ed  d0  21  
94  89  70  bc  78  33  cd  8d  - 0c  32  15  e2  29  bc  59  69  
98  6b  c2  a3  ab  80  49  57  - a9  
################INFO: Sent CT Packet ##############


################INFO: Creating MasterSecret ##############


ClientRandom::
44  44  44  44  66  66  66  66  - 66  66  66  66  66  66  66  66  
66  66  66  66  66  66  66  66  - 66  66  66  66  66  66  66  66  

ServerRandom::
15  d8  81  9d  f4  5e  48  3b  - 5e  5d  93  20  4b  78  ac  72  
76  90  23  a4  ad  79  c1  35  - ca  80  76  85  06  ca  86  39  

ckePMKey::
03  00  66  66  66  66  66  66  - 66  66  66  66  66  66  66  66  
66  66  66  66  66  66  66  66  - 66  66  66  66  66  66  66  66  
66  66  66  66  66  66  66  66  - 66  66  66  66  66  66  66  66  

MasterSecret:
65  87  19  01  d7  02  be  7b  - b7  e4  10  42  21  7e  80  64  
ac  33  db  6c  83  7f  c4  b9  - d0  32  38  d1  f6  db  3a  b6  
26  72  c6  34  1e  c0  57  bd  - 32  70  12  50  3e  65  af  1e  

################INFO: Created MasterSecret ##############


################INFO: Creating Finished Hash ##############


ClientHello:
01  00  00  29  03  00  44  44  - 44  44  66  66  66  66  66  66  
66  66  66  66  66  66  66  66  - 66  66  66  66  66  66  66  66  
66  66  66  66  66  66  00  00  - 02  00  35  01  00  
ServerHello:
02  00  00  46  03  00  15  d8  - 81  9d  f4  5e  48  3b  5e  5d  
93  20  4b  78  ac  72  76  90  - 23  a4  ad  79  c1  35  ca  80  
76  85  06  ca  86  39  20  e3  - 5a  11  e2  96  c4  40  e9  0e  
50  4e  bc  ee  9e  a8  3d  cc  - 03  57  b2  b3  ac  91  f1  76  
d0  bd  9f  e8  11  3d  a6  00  - 35  00  
Server Certificate:
0b  00  03  81  00  03  7e  00  - 03  7b  30  82  03  77  30  82  
02  e0  a0  03  02  01  02  02  - 03  13  87  19  30  0d  06  09  
2a  86  48  86  f7  0d  01  01  - 05  05  00  30  4e  31  0b  30  
09  06  03  55  04  06  13  02  - 55  53  31  10  30  0e  06  03  
55  04  0a  13  07  45  71  75  - 69  66  61  78  31  2d  30  2b  
06  03  55  04  0b  13  24  45  - 71  75  69  66  61  78  20  53  
65  63  75  72  65  20  43  65  - 72  74  69  66  69  63  61  74  
65  20  41  75  74  68  6f  72  - 69  74  79  30  1e  17  0d  31  
30  30  36  32  32  30  37  34  - 30  35  39  5a  17  0d  31  31  
30  39  32  33  31  39  32  34  - 32  35  5a  30  81  e5  31  29  
30  27  06  03  55  04  05  13  - 20  75  58  36  78  6f  35  75  
6e  6e  63  67  4d  32  72  75  - 45  56  48  59  69  76  46  4b  
38  50  58  4b  6e  2d  73  6b  - 50  31  0b  30  09  06  03  55  
04  06  13  02  55  53  31  18  - 30  16  06  03  55  04  0a  13  
0f  73  6f  75  72  63  65  66  - 6f  72  67  65  2e  6e  65  74  
31  13  30  11  06  03  55  04  - 0b  13  0a  33  37  35  34  35  
30  38  30  35  36  31  31  30  - 2f  06  03  55  04  0b  13  28  
53  65  65  20  77  77  77  2e  - 67  65  6f  74  72  75  73  74  
2e  63  6f  6d  2f  72  65  73  - 6f  75  72  63  65  73  2f  63  
70  73  20  28  63  29  31  30  - 31  2f  30  2d  06  03  55  04  
0b  13  26  44  6f  6d  61  69  - 6e  20  43  6f  6e  74  72  6f  
6c  20  56  61  6c  69  64  61  - 74  65  64  20  2d  20  51  75  
69  63  6b  53  53  4c  28  52  - 29  31  18  30  16  06  03  55  
04  03  13  0f  73  6f  75  72  - 63  65  66  6f  72  67  65  2e  
6e  65  74  30  81  9f  30  0d  - 06  09  2a  86  48  86  f7  0d  
01  01  01  05  00  03  81  8d  - 00  30  81  89  02  81  81  00  
da  38  4a  6b  65  29  33  be  - 05  4b  57  b3  bc  d4  0e  b0  
c1  41  f4  c3  a6  70  3c  ee  - ca  df  30  03  ad  b1  0b  5d  
75  56  21  4d  7b  58  64  cb  - 72  e8  5b  09  3a  21  17  8e  
5d  fa  aa  29  09  42  db  13  - 45  30  63  e5  64  da  6b  7e  
d9  d5  de  f7  bb  75  02  09  - c2  9c  ed  4e  7d  8a  83  d2  
a7  01  8c  09  23  ab  2c  48  - 67  0a  82  68  ab  e9  1f  f2  
3a  fa  18  b2  5e  ba  cc  73  - fc  7f  c0  d3  cb  f8  e4  2f  
bf  c6  1c  b7  2f  82  db  33  - ba  83  09  31  be  16  c2  a3  
02  03  01  00  01  a3  81  ca  - 30  81  c7  30  1f  06  03  55  
1d  23  04  18  30  16  80  14  - 48  e6  68  f9  2b  d2  b2  95  
d7  47  d8  23  20  10  4f  33  - 98  90  9f  d4  30  0e  06  03  
55  1d  0f  01  01  ff  04  04  - 03  02  04  f0  30  1d  06  03  
55  1d  25  04  16  30  14  06  - 08  2b  06  01  05  05  07  03  
01  06  08  2b  06  01  05  05  - 07  03  02  30  1a  06  03  55  
1d  11  04  13  30  11  82  0f  - 73  6f  75  72  63  65  66  6f  
72  67  65  2e  6e  65  74  30  - 3a  06  03  55  1d  1f  04  33  
30  31  30  2f  a0  2d  a0  2b  - 86  29  68  74  74  70  3a  2f  
2f  63  72  6c  2e  67  65  6f  - 74  72  75  73  74  2e  63  6f  
6d  2f  63  72  6c  73  2f  73  - 65  63  75  72  65  63  61  2e  
63  72  6c  30  1d  06  03  55  - 1d  0e  04  16  04  14  e7  e3  
00  04  63  28  23  3c  82  64  - 5b  6c  fa  f9  80  4d  ba  af  
ef  4e  30  0d  06  09  2a  86  - 48  86  f7  0d  01  01  05  05  
00  03  81  81  00  61  68  b4  - ac  83  6e  4e  b6  cc  7c  5b  
b0  a2  ea  d5  a1  f2  d6  a1  - 08  0e  1b  dc  f8  3a  7a  d4  
fe  c0  2d  0e  e2  12  f8  eb  - 37  d3  19  6b  c0  5e  47  cf  
29  98  1b  0a  b7  97  1f  91  - 3e  3d  71  4f  95  c8  2d  a4  
97  b6  5f  d7  a9  97  b9  73  - 4a  c9  68  ee  c0  a3  b4  3e  
fd  2d  59  9b  ba  31  77  77  - b5  17  81  c5  ce  ec  63  30  
16  9f  75  68  b2  cb  f4  83  - d0  75  51  64  8f  09  d9  a6  
2b  9d  f7  dd  af  0d  73  15  - e2  9e  df  9b  9c  8e  06  19  
39  ff  7f  c2  b9  
Server Hello Done:
0e  00  00  00  
Client Key Exchange:
10  00  00  80  56  f6  6c  60  - e8  91  6d  58  0b  54  04  32  
db  9a  dc  3c  b7  fe  a6  11  - 92  9e  d1  f4  73  d2  a2  d8  
c4  bf  c2  6a  23  6d  8b  06  - 2f  ae  96  7e  7c  6e  a9  33  
29  61  92  50  dd  24  e6  2c  - 01  94  4d  61  a7  cb  34  7d  
f4  42  08  a6  cc  fc  d9  ca  - 43  e2  c2  21  4e  6b  7e  6b  
32  e4  11  8b  99  05  fd  31  - 63  18  49  54  67  9d  d0  1f  
92  b0  91  3d  d1  af  d8  7c  - ed  d0  21  94  89  70  bc  78  
33  cd  8d  0c  32  15  e2  29  - bc  59  69  98  6b  c2  a3  ab  
80  49  57  a9  
Master Secret:
65  87  19  01  d7  02  be  7b  - b7  e4  10  42  21  7e  80  64  
ac  33  db  6c  83  7f  c4  b9  - d0  32  38  d1  f6  db  3a  b6  
26  72  c6  34  1e  c0  57  bd  - 32  70  12  50  3e  65  af  1e  

MD5 Hash:
09  9b  c5  31  a6  d0  b1  aa  - 7b  6d  61  b7  1c  66  9c  56  

SHA Hash:
7b  17  6e  66  4f  7e  70  f3  - e9  2f  1a  4a  0e  45  5c  d3  
b5  56  02  48  
ClientFinished Message:
14  00  00  24  09  9b  c5  31  - a6  d0  b1  aa  7b  6d  61  b7  
1c  66  9c  56  7b  17  6e  66  - 4f  7e  70  f3  e9  2f  1a  4a  
0e  45  5c  d3  b5  56  02  48  - 
################INFO: Created Finished Hash ##############


################INFO: Creating Key Block ##############


Key Block:
8d  9c  fe  50  ae  0e  93  0b  - 13  59  a5  4a  54  d9  2f  4f  
72  16  0f  21  b2  a7  00  b6  - ca  ed  f5  67  6f  4d  cf  a4  
b9  74  de  50  75  44  f3  68  - 27  55  de  92  80  a5  46  e2  
0f  e6  22  e8  53  96  01  f9  - 47  89  ce  d7  3e  f8  ff  2f  
00  70  ea  cc  c9  e0  ee  ba  - 0b  56  c9  31  e8  12  76  a6  
6e  84  de  27  e6  f1  48  da  - 45  f6  de  bd  09  64  be  50  
ff  3e  8f  09  86  a4  91  e2  - eb  15  76  94  4a  e8  fb  2d  
93  74  23  9c  ce  1a  7a  31  - cd  24  4d  72  26  64  40  ab  
17  ee  7f  58  0b  5d  75  c8  - dd  61  48  bd  45  54  d6  0b  

wMacPtr:
8d  9c  fe  50  ae  0e  93  0b  - 13  59  a5  4a  54  d9  2f  4f  
72  16  0f  21  
rMacPtr:
b2  a7  00  b6  ca  ed  f5  67  - 6f  4d  cf  a4  b9  74  de  50  
75  44  f3  68  
wKeyPtr:
27  55  de  92  80  a5  46  e2  - 0f  e6  22  e8  53  96  01  f9  
47  89  ce  d7  3e  f8  ff  2f  - 00  70  ea  cc  c9  e0  ee  ba  

rKeyPtr:
0b  56  c9  31  e8  12  76  a6  - 6e  84  de  27  e6  f1  48  da  
45  f6  de  bd  09  64  be  50  - ff  3e  8f  09  86  a4  91  e2  

wIVPtr:
eb  15  76  94  4a  e8  fb  2d  - 93  74  23  9c  ce  1a  7a  31  

rIVPtr:
cd  24  4d  72  26  64  40  ab  - 17  ee  7f  58  0b  5d  75  c8  

################INFO: Created Key Block ##############


WIV :
eb  15  76  94  4a  e8  fb  2d  - 93  74  23  9c  ce  1a  7a  31  

RIV :
cd  24  4d  72  26  64  40  ab  - 17  ee  7f  58  0b  5d  75  c8  

################INFO: Sending SSL Packet ##############


Record Length:
00  28  
Record:
14  00  00  24  09  9b  c5  31  - a6  d0  b1  aa  7b  6d  61  b7  
1c  66  9c  56  7b  17  6e  66  - 4f  7e  70  f3  e9  2f  1a  4a  
0e  45  5c  d3  b5  56  02  48  - 
Intermediate MAC:
b2  35  fc  ef  d7  4f  eb  37  - 12  4c  a0  bd  da  27  43  c7  
f9  ed  ed  fc  
Final MAC:
f8  81  f9  b0  94  3c  95  68  - bd  3a  56  67  24  47  1e  dd  
3b  d0  58  47  
Padding Length: 4

Padding:
03  03  03  03  
Record + MAC:
14  00  00  24  09  9b  c5  31  - a6  d0  b1  aa  7b  6d  61  b7  
1c  66  9c  56  7b  17  6e  66  - 4f  7e  70  f3  e9  2f  1a  4a  
0e  45  5c  d3  b5  56  02  48  - f8  81  f9  b0  94  3c  95  68  
bd  3a  56  67  24  47  1e  dd  - 3b  d0  58  47  03  03  03  03  

Encrypted Record + MAC:
21  69  2a  1c  8c  72  c4  39  - c4  b4  d1  cf  f1  0b  19  08  
7c  72  6f  76  08  d4  7c  d6  - a6  69  1d  4b  fa  02  6c  70  
c1  29  a4  fa  eb  9b  cb  ed  - ed  1b  68  e6  5e  7e  e4  85  
3b  8c  a6  20  04  85  91  f2  - 17  36  58  e7  d5  73  d3  14  

Packet Sent:
16  03  00  00  40  21  69  2a  - 1c  8c  72  c4  39  c4  b4  d1  
cf  f1  0b  19  08  7c  72  6f  - 76  08  d4  7c  d6  a6  69  1d  
4b  fa  02  6c  70  c1  29  a4  - fa  eb  9b  cb  ed  ed  1b  68  
e6  5e  7e  e4  85  3b  8c  a6  - 20  04  85  91  f2  17  36  58  
e7  d5  73  d3  14  
################INFO: Sent SSL Packet ##############


WIV :
3b  8c  a6  20  04  85  91  f2  - 17  36  58  e7  d5  73  d3  14  

RIV :
cd  24  4d  72  26  64  40  ab  - 17  ee  7f  58  0b  5d  75  c8  

################INFO: Reading ServerFinished from server ##############


INFO: Received Server Change Cipher Spec
Len = 1

INFO: Received ServerFinished Message of Length: 64


INFO: Finished Read from Server:
48  ce  ea  53  cc  71  d1  e1  - de  a4  da  34  63  5c  0c  21  
d6  68  49  8c  ab  03  e9  40  - bb  6f  d2  db  d3  a7  1c  0b  
25  f4  c3  33  4f  93  62  2c  - 33  7a  6e  6d  27  89  da  79  
84  7b  19  a5  fd  9c  76  63  - 72  3d  f5  7a  a9  89  12  47  


INFO: Decrypted Finished Message from Server:
14  00  00  24  1b  a1  7c  3d  - 6a  df  32  55  85  e2  ac  62  
ef  f5  5b  1d  de  cb  38  76  - 89  93  3e  c1  91  64  dd  45  
a0  62  d5  ad  99  91  38  f3  - 
################INFO: Read ServerFinished from server ##############


WIV :
3b  8c  a6  20  04  85  91  f2  - 17  36  58  e7  d5  73  d3  14  

RIV :
84  7b  19  a5  fd  9c  76  63  - 72  3d  f5  7a  a9  89  12  47  
Request Length:  18

Sending Request:
47  45  54  20  2f  20  48  54  - 54  50  2f  31  2e  31  0d  0a  
0d  0a  
################INFO: Sending SSL Record Packet ##############


Record Length:
00  12  
Record:
47  45  54  20  2f  20  48  54  - 54  50  2f  31  2e  31  0d  0a  
0d  0a  
Intermediate MAC:
29  3f  99  48  ac  22  e6  37  - 38  9e  a5  dc  56  f1  9e  aa  
e9  f2  3c  41  
Final MAC:
09  17  a3  ae  fc  bb  de  4b  - f9  2c  84  48  2b  6a  6d  87  
47  8f  6e  4c  
Padding Length: 10

Padding:
09  09  09  09  09  09  09  09  - 09  09  
Record + MAC:
47  45  54  20  2f  20  48  54  - 54  50  2f  31  2e  31  0d  0a  
0d  0a  09  17  a3  ae  fc  bb  - de  4b  f9  2c  84  48  2b  6a  
6d  87  47  8f  6e  4c  09  09  - 09  09  09  09  09  09  09  09  

Encrypted Record + MAC:
fa  1a  6b  68  e8  c9  cb  41  - 2b  d5  94  07  17  cd  2f  0c  
c5  f1  e3  eb  7a  e4  cd  53  - 61  62  47  c0  d2  de  fd  c1  
d1  06  00  b9  5e  22  39  42  - 77  fd  b5  7a  8b  94  2e  84  

Packet Sent:
17  03  00  00  30  fa  1a  6b  - 68  e8  c9  cb  41  2b  d5  94  
07  17  cd  2f  0c  c5  f1  e3  - eb  7a  e4  cd  53  61  62  47  
c0  d2  de  fd  c1  d1  06  00  - b9  5e  22  39  42  77  fd  b5  
7a  8b  94  2e  84  
################INFO: Sent SSL Record Packet ##############


WIV :
d1  06  00  b9  5e  22  39  42  - 77  fd  b5  7a  8b  94  2e  84  

RIV :
84  7b  19  a5  fd  9c  76  63  - 72  3d  f5  7a  a9  89  12  47  

################INFO: Reading SSL Packet ##############


Encrypted Data:
b1  34  1e  71  d8  c9  50  a0  - 9c  ed  1c  a8  2d  5f  aa  ca  
59  8c  98  db  7f  0b  8b  b8  - ce  19  2d  b6  41  49  63  81  
f9  17  61  5a  66  69  e0  d3  - da  95  a7  6b  19  ca  d4  5f  
d5  ec  00  4a  90  48  ee  ff  - 3c  9e  34  bc  81  87  e2  6c  
cc  c6  db  cc  62  08  3c  a8  - 1b  64  93  d5  16  dc  3f  b8  
e6  f6  a7  79  38  a5  a2  f9  - e3  b1  7c  75  e7  c5  16  de  
96  db  b5  fd  7b  e4  50  26  - c0  7d  0f  37  6c  da  de  8b  
b9  f5  d2  6b  81  61  35  87  - c2  09  46  56  20  ab  d6  3c  
b6  49  57  4c  02  cd  c3  ee  - 89  d0  85  5b  fb  7d  54  e1  

Length of encrypted data: 144 


PlainText Data:
HTTP/1.0 302 Found
Location: https://sourceforge.net/
Server: BigIP
Connection: close
Content-Length: 0

~���H�.�G�
          9�=ϑ�















DecryptedData:
48  54  54  50  2f  31  2e  30  - 20  33  30  32  20  46  6f  75  
6e  64  0d  0a  4c  6f  63  61  - 74  69  6f  6e  3a  20  68  74  
74  70  73  3a  2f  2f  73  6f  - 75  72  63  65  66  6f  72  67  
65  2e  6e  65  74  2f  0d  0a  - 53  65  72  76  65  72  3a  20  
42  69  67  49  50  0d  0a  43  - 6f  6e  6e  65  63  74  69  6f  
6e  3a  20  63  6c  6f  73  65  - 0d  0a  43  6f  6e  74  65  6e  
74  2d  4c  65  6e  67  74  68  - 3a  20  30  0d  0a  0d  0a  7e  
ea  a0  e1  48  de  2e  96  00  - 47  f7  0c  39  14  e8  02  3d  
cf  91  db  0c  0c  0c  0c  0c  - 0c  0c  0c  0c  0c  0c  0c  0c  

################INFO: Read SSL Packet ##############


WIV :
d1  06  00  b9  5e  22  39  42  - 77  fd  b5  7a  8b  94  2e  84  

RIV :
b6  49  57  4c  02  cd  c3  ee  - 89  d0  85  5b  fb  7d  54  e1  
root@family:/home/family/sslfuzzerpython-read-only/AES-Encryption# 

```