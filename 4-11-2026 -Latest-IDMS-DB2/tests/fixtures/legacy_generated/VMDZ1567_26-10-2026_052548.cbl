000010 CBL ARITH(EXTEND)                                                00010000
000020 IDENTIFICATION DIVISION.                                         00020000
000030*-----------------------.                                         00030000
000040 PROGRAM-ID. VMDZ1567.                                            00040000
000050 AUTHOR.       PYTHON-AUTOMATION-USING-AI.                        00050000
000060 DATE-WRITTEN. 2026-10-26.                                        00060000
000070 DATE-COMPILED.                                                   00070000
000080                                                                  00080000
000090****************************************************************  00090000
000100*REMARKS.       AANDUIDEN BOEKING IN DB FORMULIER              *  00100000
000110*               VOOR EFFECTENDOSSIERS.                         *  00110000
000120*                                                              *  00120000
000130*COMMITS        MICHELINE BEEVERS (DATAPROCESS BELGIUM).       *  00130000
000140*                                                              *  00140000
000150*  MODIFIED BY J.CLEMENT                                       *  00150000
000160*  07/92 : AANPASSING SLIK : RECORDS 475 ---> 575              *  00160000
000170*                            VMBD510C    ---> VMBD510V         *  00170000
000180*                                                              *  00180000
000190*  MODIFIED BY S. POMPONIO                                     *  00190000
000200*  01/97 : AANPASSING EURO2000 : RECORDS 750 ---> 1050         *  00200000
000210*                                VMBD510V    ---> VMBD510X     *  00210000
000220*                                DATEPARM EN 8 POSITIONS       *  00220000
000230*                                                              *  00230000
000240*  MODIFIED BY JEROEN "JEROD" DE SCHUTTER (DOLMEN) :           *  00240000
000250*  08/2003 : AANPASSINGEN IKV. INTEGRATIEPROJECT 6212 :        *  00250000
000260*            DAISY SECURITIES KASBONS : VMBD510X --> VMBD205I  *  00260000
000270*                                                              *  00270000
000280****************************************************************  00280000
000290                                                                  00290000
000300 ENVIRONMENT DIVISION.                                            00300000
000310*--------------------.                                            00310000
000320 CONFIGURATION SECTION.                                           00320000
000330 SPECIAL-NAMES.                                                   00330000
000340     DECIMAL-POINT IS COMMA.                                      00340000
000350 INPUT-OUTPUT SECTION.                                            00350000
000360 FILE-CONTROL.                                                    00360000
000370     SELECT OPERATIES ASSIGN TO UT-S-DD010.                       00370000
000380                                                                  00380000
000390 DATA DIVISION.                                                   00390000
000400*-------------.                                                   00400000
000410 FILE SECTION.                                                    00410000
000420 FD   OPERATIES                                                   00420000
000430      BLOCK CONTAINS 0 RECORDS                                    00430000
000440      RECORD CONTAINS 1200 CHARACTERS                             00440000
000450      RECORDING F                                                 00450000
000460      LABEL RECORDS STANDARD.                                     00460000
000470 01   OPERATIES-REC             PIC X(1200).                      00470000
000480                                                                  00480000
000490                                                                  00490000
000500 WORKING-STORAGE SECTION.                                         00500000
000510     EXEC SQL INCLUDE DZ01RSTV END-EXEC.                          00510000
000520                                                                  00520000
000530 01  WS-SWITCHES.                                                 00530000
000540     02  SW-VMDZ205I            PIC X     VALUE 'N'.              00540000
000550         88  VMDZ205I-NOT-EOF       VALUE 'N'.                    00550000
000560         88  VMDZ205I-EOF           VALUE 'Y'.                    00560000
000570                                                                  00570000
000580 01  HELP-VARIABLE.                                               00580000
000590     02  WS-RESTART-REC.                                          00590000
000600         03  NB-READ            PIC 9(15)   VALUE ZERO.           00600000
000610         03  KY-RESTART         PIC X(1200) VALUE SPACES.         00610000
000620     02  WS-INPUT-KASBONS       PIC X(1200) VALUE SPACES.         00620000
000630     02  WS-TELLER              PIC 9(9)   COMP-3 VALUE ZERO.     00630000
000640     02  WS-NB-INPUT-UPD-I      PIC 9(7)   COMP-3 VALUE ZERO.     00640000
000650     02  WS-NB-BFAR-UPD-I       PIC S9(11) COMP-3 VALUE +0.       00650000
000660                                                                  00660000
000670 01  WS-DATE-CONVERSION.                                          00670000
000680     03  DA-YYMMDD.                                               00680000
000690         05  YY                     PIC 99    VALUE ZERO.         00690000
000700         05  MM                     PIC 99    VALUE ZERO.         00700000
000710         05  DD                     PIC 99    VALUE ZERO.         00710000
000720     03  DA-DDMMCCYY.                                             00720000
000730         05  DD                     PIC 99    VALUE ZERO.         00730000
000740         05  MM                     PIC 99    VALUE ZERO.         00740000
000750         05  CC                     PIC 99    VALUE ZERO.         00750000
000760         05  YY                     PIC 99    VALUE ZERO.         00760000
000770     03  DA-CCYYMMDD.                                             00770000
000780         05  CC                     PIC 99    VALUE ZERO.         00780000
000790         05  YY                     PIC 99    VALUE ZERO.         00790000
000800         05  MM                     PIC 99    VALUE ZERO.         00800000
000810         05  DD                     PIC 99    VALUE ZERO.         00810000
000820     03  DA-CCYYMMDD-R REDEFINES DA-CCYYMMDD.                     00820000
000830         05  CCYY                   PIC 9999.                     00830000
000840         05  MM                     PIC 99.                       00840000
000850         05  DD                     PIC 99.                       00850000
000860     03  DA-DD-MM-CCYY.                                           00860000
000870         05  DD                     PIC 9(02).                    00870000
000880         05  TE-MARKER1             PIC X     VALUE '.'.          00880000
000890         05  MM                     PIC 9(02).                    00890000
000900         05  TE-MARKER2             PIC X     VALUE '.'.          00900000
000910         05  CCYY                   PIC 9(04).                    00910000
000920 77  USERABEN                   PIC X(8) VALUE 'USERABEN'.        00920000
000930                                                                  00930000
000940 01  STOP-DATONLY.                                                00940000
000950     02  DATE-YMD.                                                00950000
000960         03  D-YEAR             PIC 99.                           00960000
000970         03  D-MONTH            PIC 99.                           00970000
000980         03  D-DAY              PIC 99.                           00980000
000990     02  DATE-DMY.                                                00990000
001000         03  D-DAY              PIC 99.                           01000000
001010         03  D-MONTH            PIC 99.                           01010000
001020         03  D-YEAR             PIC 99.                           01020000
001030     02  DATE-YMD8.                                               01030000
001040         03  D-CENT             PIC 99.                           01040000
001050         03  D-YEAR             PIC 99.                           01050000
001060         03  D-MONTH            PIC 99.                           01060000
001070         03  D-DAY              PIC 99.                           01070000
001080     02  DATE-DMY8.                                               01080000
001090         03  D-DAY              PIC 99.                           01090000
001100         03  D-MONTH            PIC 99.                           01100000
001110         03  D-CENT             PIC 99.                           01110000
001120         03  D-YEAR             PIC 99.                           01120000
001130                                                                  01130000
001140     COPY VMDZ205I.                                               01140000
001150                                                                  01150000
001160                                                                  01160000
001170     EXEC SQL INCLUDE SQLERRWS END-EXEC.                          01170000
001180     EXEC SQL INCLUDE SQLCA END-EXEC.                             01180000
001190     EXEC SQL INCLUDE DZBFARTV END-EXEC.                          01190000
001200                                                                  01200000
001210                                                                  01210000
001220 01  WS-DB2-GENERATED.                                            01220000
001230     10  CS-PROGRAM               PIC X(8)    VALUE 'VMDZ1567'.   01230000
001240                                                                  01240000
001250 01  WS-TIMESTAMP-FIELDS.                                         01250000
001260     05 TS-SYSTEM.                                                01260000
001270        10  DA-SYS.                                               01270000
001280            15  DA-SYS-CCYY.                                      01280000
001290                20  CC            PIC X(2).                       01290000
001300                20  YY            PIC X(2).                       01300000
001310            15  MM                PIC X(2).                       01310000
001320            15  DD                PIC X(2).                       01320000
001330        10  HR-SYS.                                               01330000
001340            15  HH                PIC X(2).                       01340000
001350            15  MI                PIC X(2).                       01350000
001360            15  SS                PIC X(2).                       01360000
001370            15  TT                PIC X(2).                       01370000
001380     05 TS-TIMESTAMP.                                             01380000
001390        10  CC                    PIC X(2).                       01390000
001400        10  YY                    PIC X(2).                       01400000
001410        10  TE-MARKER1            PIC X             VALUE '-'.    01410000
001420        10  MM                    PIC X(2).                       01420000
001430        10  TE-MARKER2            PIC X             VALUE '-'.    01430000
001440        10  DD                    PIC X(2).                       01440000
001450        10  TE-MARKER3            PIC X             VALUE '-'.    01450000
001460        10  HH                    PIC X(2).                       01460000
001470        10  TE-MARKER4            PIC X             VALUE '.'.    01470000
001480        10  MI                    PIC X(2).                       01480000
001490        10  TE-MARKER5            PIC X             VALUE '.'.    01490000
001500        10  SS                    PIC X(2).                       01500000
001510        10  TE-MARKER6            PIC X             VALUE '.'.    01510000
001520        10  TT                    PIC X(2).                       01520000
001530        10  NNNN                  PIC 9(04)         VALUE 0.      01530000
001540                                                                  01540000
001550                                                                  01550000
001560 LINKAGE SECTION.                                                 01560000
001570 01  PARAM-DATONLY.                                               01570000
001580     03  L-PARAM                PIC S9(4) COMP.                   01580000
001590     03  DATUMLS.                                                 01590000
001600         05  DATE-IND           PIC X.                            01600000
001610         05  DATE8-LS           PIC X(8).                         01610000
001620                                                                  01620000
001630 PROCEDURE DIVISION USING PARAM-DATONLY.                          01630000
001640*--------------------------------------.                          01640000
001650*                                                                 01650000
001660* INITIALISATIE                                                   01660000
001670*                                                                 01670000
001680     PERFORM 600-GET-TIMESTAMP.                                   01680000
001690     MOVE DATE8-LS       TO DATE-DMY8.                            01690000
001700     MOVE CORR DATE-DMY8 TO DATE-YMD.                             01700000
001710     MOVE CORR DATE-DMY8 TO DATE-DMY.                             01710000
001720     MOVE CORR DATE-DMY8 TO DATE-YMD8.                            01720000
001730                                                                  01730000
001740     MOVE CS-PROGRAM   TO PROGRAM-NAME.                           01740000
001750     SET VMDZ205I-NOT-EOF TO TRUE.                                01750000
001760     INITIALIZE HELP-VARIABLE.                                    01760000
001770     MOVE ZEROES TO DA-CCYYMMDD.                                  01770000
001780     MOVE DATE-YMD8 TO DA-CCYYMMDD.                               01780000
001790     MOVE CORR DA-CCYYMMDD-R TO DA-DD-MM-CCYY.                    01790000
001800                                                                  01800000
001810     OPEN INPUT OPERATIES.                                        01810000
001820                                                                  01820000
001830     PERFORM 700-RESTART-CONTROL.                                 01830000
001840                                                                  01840000
001850     PERFORM READ-FLAT-FILE.                                      01850000
001860                                                                  01860000
001870     PERFORM VERWERKING UNTIL VMDZ205I-EOF.                       01870000
001880                                                                  01880000
001890     PERFORM 800-PROCESS-COMMIT.                                  01890000
001900                                                                  01900000
001910     DISPLAY 'NUMBER OF RECORDS PROCESSED : ' WS-NB-INPUT-UPD-I.  01910000
001920     DISPLAY 'NUMBER OF UPDATE BFAR       : ' WS-NB-BFAR-UPD-I.   01920000
001930     CLOSE OPERATIES.                                             01930000
001940     STOP RUN.                                                    01940000
001950 VERWERKING.                                                      01950000
001960*-----------                                                      01960000
001970     INITIALIZE DCLDZBFARTV.                                      01970000
001980     MOVE '1815' TO CT-TGDSERV-479BFAR OF DCLDZBFARTV             01980000
001990     MOVE NR-CIO-FORM-AS-R TO NR-CIOFMAS-479BFAR OF DCLDZBFARTV   01990000
002000     MOVE ZEROES TO DA-CCYYMMDD                                   02000000
002010     MOVE DA-CREA-FORM-AS-R TO DA-CCYYMMDD                        02010000
002020     IF DA-CCYYMMDD = ZERO OR DA-CCYYMMDD = SPACES                02020000
002030        MOVE 00010101 TO DA-CCYYMMDD                              02030000
002040     END-IF                                                       02040000
002050     MOVE CORR DA-CCYYMMDD-R TO DA-DD-MM-CCYY                     02050000
002060     MOVE DA-DD-MM-CCYY TO DA-CRFMAS-479BFAR OF DCLDZBFARTV       02060000
002070     MOVE NR-ID-FORM-AS OF VMDZ205I TO NR-IDFMAS-479BFAR          02070000
002080       OF DCLDZBFARTV                                             02080000
002090     MOVE CT-OPG-FORM-AS-R TO CT-OPGFMAS-479BFAR OF DCLDZBFARTV   02090000
002100     MOVE CT-OPD-FORM-AS-R TO CT-OPDFMAS-479BFAR OF DCLDZBFARTV   02100000
002110     MOVE ZEROES TO DA-CCYYMMDD                                   02110000
002120     MOVE DATE-YMD8 TO DA-CCYYMMDD                                02120000
002130     MOVE CORR DA-CCYYMMDD-R TO DA-DD-MM-CCYY                     02130000
002140     MOVE DA-DD-MM-CCYY TO DA-INFSDGD-479BFAR OF DCLDZBFARTV      02140000
002150     MOVE SQL-STATEMENT TO SQL-LOCATION                           02150000
002160     PERFORM 1100-UPDATE-DZBFAR.                                  02160000
002170                                                                  02170000
002180*    LEZEN VAN DE INVOER                                          02180000
002190                                                                  02190000
002200                                                                  02200000
002210     IF WS-TELLER > 99                                            02210000
002220        PERFORM 800-PROCESS-COMMIT                                02220000
002230     END-IF.                                                      02230000
002240                                                                  02240000
002250     PERFORM READ-FLAT-FILE.                                      02250000
002260 READ-FLAT-FILE.                                                  02260000
002270     INITIALIZE VMDZ205I.                                         02270000
002280                                                                  02280000
002290     READ OPERATIES INTO VMDZ205I                                 02290000
002300        AT END SET VMDZ205I-EOF TO TRUE.                          02300000
002310                                                                  02310000
002320        IF VMDZ205I-NOT-EOF                                       02320000
002330           THEN                                                   02330000
002340           ADD +1 TO WS-TELLER                                    02340000
002350           ADD +1 TO WS-NB-INPUT-UPD-I                            02350000
002360           MOVE VMDZ205I TO WS-INPUT-KASBONS                      02360000
002370        END-IF.                                                   02370000
002380                                                                  02380000
002390 600-GET-TIMESTAMP.                                               02390000
002400D    DISPLAY '600-GET-TIMESTAMP.'                                 02400000
002410     MOVE FUNCTION CURRENT-DATE TO TS-SYSTEM.                     02410000
002420     MOVE CC OF TS-SYSTEM       TO CC OF TS-TIMESTAMP             02420000
002430     MOVE YY OF TS-SYSTEM       TO YY OF TS-TIMESTAMP             02430000
002440     MOVE MM OF TS-SYSTEM       TO MM OF TS-TIMESTAMP             02440000
002450     MOVE DD OF TS-SYSTEM       TO DD OF TS-TIMESTAMP             02450000
002460     MOVE HH OF TS-SYSTEM       TO HH OF TS-TIMESTAMP             02460000
002470     MOVE MI OF TS-SYSTEM       TO MI OF TS-TIMESTAMP             02470000
002480     MOVE SS OF TS-SYSTEM       TO SS OF TS-TIMESTAMP             02480000
002490     MOVE TT OF TS-SYSTEM       TO TT OF TS-TIMESTAMP             02490000
002500     DISPLAY 'TIMESTAMP: ' TS-TIMESTAMP                           02500000
002510     .                                                            02510000
002520                                                                  02520000
002530                                                                  02530000
002540 1100-UPDATE-DZBFAR.                                              02540000
002550                                                                  02550000
002560     MOVE TS-TIMESTAMP TO TS-UPDATE-479BFAR OF DCLDZBFARTV        02560000
002570     MOVE CS-PROGRAM TO ID-USERID-479BFAR OF DCLDZBFARTV          02570000
002580             MOVE 1100 TO SQL-LOCATION                            02580000
002590     EXEC SQL                                                     02590000
002600        UPDATE DZBFARTV                                           02600000
002610        SET                                                       02610000
002620        DA_INFSDGD_479BFAR = :DCLDZBFARTV.DA-INFSDGD-479BFAR,     02620000
002630        TS_UPDATE_479BFAR = :DCLDZBFARTV.TS-UPDATE-479BFAR,       02630000
002640        ID_USERID_479BFAR = :DCLDZBFARTV.ID-USERID-479BFAR        02640000
002650        WHERE                                                     02650000
002660        CT_TGDSERV_479BFAR = :DCLDZBFARTV.CT-TGDSERV-479BFAR      02660000
002670        AND NR_CIOFMAS_479BFAR = :DCLDZBFARTV.NR-CIOFMAS-479BFAR  02670000
002680        AND DA_CRFMAS_479BFAR = :DCLDZBFARTV.DA-CRFMAS-479BFAR    02680000
002690        AND NR_IDFMAS_479BFAR = :DCLDZBFARTV.NR-IDFMAS-479BFAR    02690000
002700        AND CT_OPDFMAS_479BFAR = :DCLDZBFARTV.CT-OPDFMAS-479BFAR  02700000
002710        AND CT_OPGFMAS_479BFAR = :DCLDZBFARTV.CT-OPGFMAS-479BFAR  02710000
002720        QUERYNO 442                                               02720000
002730     END-EXEC                                                     02730000
002740     EVALUATE SQLCODE                                             02740000
002750       WHEN 0                                                     02750000
002760            ADD 1 TO WS-NB-BFAR-UPD-I                             02760000
002770       WHEN OTHER                                                 02770000
002780            DISPLAY 'ERROR ON UPDATE DZBFARTV'                    02780000
002790            PERFORM SQLERROR                                      02790000
002800     END-EVALUATE                                                 02800000
002810     .                                                            02810000
002820                                                                  02820000
002830*SQLERROR ROUTINE.                                                02830000
002840     EXEC SQL                                                     02840000
002850        INCLUDE SQLERROR                                          02850000
002860     END-EXEC.                                                    02860000
002870                                                                  02870000
002880 700-RESTART-CONTROL.                                             02880000
002890     MOVE CS-PROGRAM TO NM-ID-RS-PROGRAM OF DCLDZ01RSTV.          02890000
002900     MOVE DA-DD-MM-CCYY   TO DA-CR-RS       OF DCLDZ01RSTV.       02900000
002910     MOVE 1     TO NB-ID-RS-PHASE      OF DCLDZ01RSTV.            02910000
002920                                                                  02920000
002930     PERFORM 700-SELECT-DZ01RSTV.                                 02930000
002940                                                                  02940000
002950     EVALUATE SQLCODE                                             02950000
002960       WHEN 0        PERFORM 710-JOB-IS-RESTART                   02960000
002970       WHEN 100 PERFORM 720-WRITE-RESTART-REC                     02970000
002980       WHEN OTHER               PERFORM SQLERROR                  02980000
002990     END-EVALUATE.                                                02990000
003000                                                                  03000000
003010     MOVE 0 TO WS-TELLER.                                         03010000
003020                                                                  03020000
003030 700-SELECT-DZ01RSTV.                                             03030000
003040                                                                  03040000
003050     MOVE 700 TO SQL-LOCATION                                     03050000
003060     EXEC SQL                                                     03060000
003070      SELECT NM_ID_RS_PROGRAM                                     03070000
003080           , NB_ID_RS_PHASE                                       03080000
003090           , DA_CR_RS                                             03090000
003100           , CO_ID_RS                                             03100000
003110           , NB_DAY_RS                                            03110000
003120           , TE_CH_RS_DATA                                        03120000
003130        INTO :DCLDZ01RSTV.NM-ID-RS-PROGRAM                        03130000
003140           , :DCLDZ01RSTV.NB-ID-RS-PHASE                          03140000
003150           , :DCLDZ01RSTV.DA-CR-RS                                03150000
003160           , :DCLDZ01RSTV.CO-ID-RS                                03160000
003170           , :DCLDZ01RSTV.NB-DAY-RS                               03170000
003180           , :DCLDZ01RSTV.TE-CH-RS-DATA                           03180000
003190        FROM DZ01RSTV                                             03190000
003200       WHERE NM_ID_RS_PROGRAM = :DCLDZ01RSTV.NM-ID-RS-PROGRAM     03200000
003210         AND NB_ID_RS_PHASE = :DCLDZ01RSTV.NB-ID-RS-PHASE         03210000
003220         AND DA_CR_RS = :DCLDZ01RSTV.DA-CR-RS                     03220000
003230      QUERYNO 376                                                 03230000
003240     END-EXEC                                                     03240000
003250                                                                  03250000
003260     EVALUATE SQLCODE                                             03260000
003270       WHEN 0                                                     03270000
003280       WHEN 100                                                   03280000
003290            CONTINUE                                              03290000
003300       WHEN OTHER                                                 03300000
003310            DISPLAY 'ERROR ON SELECT DZ01RSTV'                    03310000
003320            PERFORM SQLERROR                                      03320000
003330     END-EVALUATE                                                 03330000
003340     .                                                            03340000
003350                                                                  03350000
003360 700-UPDATE-DZ01RSTV.                                             03360000
003370                                                                  03370000
003380     MOVE 700 TO SQL-LOCATION                                     03380000
003390     EXEC SQL                                                     03390000
003400      UPDATE DZ01RSTV                                             03400000
003410         SET TE_CH_RS_DATA = :DCLDZ01RSTV.TE-CH-RS-DATA           03410000
003420           , CO_ID_RS = :DCLDZ01RSTV.CO-ID-RS                     03420000
003430       WHERE NM_ID_RS_PROGRAM = :DCLDZ01RSTV.NM-ID-RS-PROGRAM     03430000
003440         AND NB_ID_RS_PHASE = :DCLDZ01RSTV.NB-ID-RS-PHASE         03440000
003450         AND DA_CR_RS = :DCLDZ01RSTV.DA-CR-RS                     03450000
003460      QUERYNO 398                                                 03460000
003470     END-EXEC                                                     03470000
003480                                                                  03480000
003490     EVALUATE SQLCODE                                             03490000
003500       WHEN 0                                                     03500000
003510            CONTINUE                                              03510000
003520       WHEN OTHER                                                 03520000
003530            DISPLAY 'ERROR ON UPDATE DZ01RSTV'                    03530000
003540            PERFORM SQLERROR                                      03540000
003550     END-EVALUATE                                                 03550000
003560     .                                                            03560000
003570                                                                  03570000
003580 700-INSERT-DZ01RSTV.                                             03580000
003590                                                                  03590000
003600     MOVE 700 TO SQL-LOCATION                                     03600000
003610     EXEC SQL                                                     03610000
003620      INSERT INTO DZ01RSTV                                        03620000
003630             VALUES (:DCLDZ01RSTV)                                03630000
003640     END-EXEC                                                     03640000
003650                                                                  03650000
003660     EVALUATE SQLCODE                                             03660000
003670       WHEN 0                                                     03670000
003680            CONTINUE                                              03680000
003690       WHEN OTHER                                                 03690000
003700            DISPLAY 'ERROR ON INSERT DZ01RSTV'                    03700000
003710            PERFORM SQLERROR                                      03710000
003720     END-EVALUATE                                                 03720000
003730     .                                                            03730000
003740                                                                  03740000
003750 710-JOB-IS-RESTART.                                              03750000
003760     MOVE TE-CH-RS-DATA-TEXT OF DCLDZ01RSTV                       03760000
003770       TO WS-RESTART-REC.                                         03770000
003780                                                                  03780000
003790     IF CO-ID-RS OF DCLDZ01RSTV = '1'                             03790000
003800        THEN DISPLAY ' PREVIOUS RUN COMPLETE '                    03800000
003810        PERFORM 810000-CALL-USERABEN                              03810000
003820     ELSE PERFORM NB-READ OF WS-RESTART-REC TIMES                 03820000
003830        PERFORM READ-FLAT-FILE                                    03830000
003840        MOVE NB-READ OF WS-RESTART-REC                            03840000
003850            TO WS-NB-INPUT-UPD-I                                  03850000
003860     END-PERFORM                                                  03860000
003870     END-IF.                                                      03870000
003880                                                                  03880000
003890 720-WRITE-RESTART-REC.                                           03890000
003900     MOVE '0' TO CO-ID-RS    OF DCLDZ01RSTV.                      03900000
003910     MOVE 7      TO NB-DAY-RS OF DCLDZ01RSTV.                     03910000
003920     MOVE 0                     TO WS-NB-INPUT-UPD-I.             03920000
003930     MOVE WS-NB-INPUT-UPD-I       TO NB-READ OF WS-RESTART-REC.   03930000
003940     INITIALIZE KY-RESTART.                                       03940000
003950     MOVE 1215                                                    03950000
003960       TO TE-CH-RS-DATA-LEN OF DCLDZ01RSTV.                       03960000
003970     MOVE WS-RESTART-REC                                          03970000
003980       TO TE-CH-RS-DATA-TEXT   OF DCLDZ01RSTV.                    03980000
003990                                                                  03990000
004000     PERFORM 700-INSERT-DZ01RSTV.                                 04000000
004010                                                                  04010000
004020 800-PROCESS-COMMIT.                                              04020000
004030     MOVE 0               TO WS-TELLER.                           04030000
004040     MOVE WS-NB-INPUT-UPD-I TO NB-READ  OF WS-RESTART-REC.        04040000
004050     MOVE WS-INPUT-KASBONS                                        04050000
004060       TO KY-RESTART OF WS-RESTART-REC.                           04060000
004070                                                                  04070000
004080     IF VMDZ205I-EOF                                              04080000
004090        THEN MOVE '1'   TO CO-ID-RS OF DCLDZ01RSTV                04090000
004100     ELSE MOVE '0' TO CO-ID-RS OF DCLDZ01RSTV                     04100000
004110     END-IF.                                                      04110000
004120                                                                  04120000
004130     MOVE 15                                                      04130000
004140       TO TE-CH-RS-DATA-LEN OF DCLDZ01RSTV.                       04140000
004150     MOVE WS-RESTART-REC                                          04150000
004160       TO TE-CH-RS-DATA-TEXT   OF DCLDZ01RSTV.                    04160000
004170                                                                  04170000
004180     PERFORM 700-UPDATE-DZ01RSTV.                                 04180000
004190                                                                  04190000
004200     MOVE 800 TO SQL-LOCATION                                     04200000
004210     EXEC SQL                                                     04210000
004220      COMMIT                                                      04220000
004230     END-EXEC.                                                    04230000
004240                                                                  04240000
004250     EVALUATE SQLCODE                                             04250000
004260       WHEN 0                                                     04260000
004270            CONTINUE                                              04270000
004280       WHEN OTHER                                                 04280000
004290            DISPLAY 'ERROR REC NUMBER : ' WS-NB-INPUT-UPD-I       04290000
004300            PERFORM SQLERROR                                      04300000
004310     END-EVALUATE.                                                04310000
004320                                                                  04320000
004330 810000-CALL-USERABEN.                                            04330000
004340     CALL USERABEN.                                               04340000
