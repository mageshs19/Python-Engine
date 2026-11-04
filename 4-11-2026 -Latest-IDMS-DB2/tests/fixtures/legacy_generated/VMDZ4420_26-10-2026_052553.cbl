000010 CBL ARITH(EXTEND)                                                00010000
000020 IDENTIFICATION DIVISION.                                         00020000
000030*------------------------                                         00030000
000040 PROGRAM-ID. VMDZ4420.                                            00040000
000050 AUTHOR.       PYTHON-AUTOMATION-USING-AI.                        00050000
000060 DATE-WRITTEN. 2026-10-26.                                        00060000
000070*                                                                 00070000
000080******************************************************************00080000
000090*                                                                *00090000
000100*                INFORMATORISCHE KASBON 2.                       *00100000
000110*                                                                *00110000
000120******************************************************************00120000
000130*                                                                *00130000
000140*                VERGELIJKING DATABASE EN INVENTARIS             *00140000
000150*                -----------------------------------             *00150000
000160*                                                                *00160000
000170*                TWEEDE PROGRAMMA :                              *00170000
000180*                                                                *00180000
000190*                OPZOEKEN VAN ALLE EFFECTEN EN ALLE EVENEMENTEN  *00190000
000200*                DIE NOG IN LEVEN ZIJN.                          *00200000
000210*                                                                *00210000
000220* 01/06/92 : DE SCHEPPER KOEN (HCS AS) - PROBLEM RECORD 436451   *00220000
000230*            WAARDEN DIE NOG IN STOCK ZIJN MOGEN NIET MEEGENOMEN *00230000
000240*            WORDEN IN HET OUTPUTBESTAND.                        *00240000
000250*                                                                *00250000
000260* 16/06/92 : DE SCHEPPER KOEN (HCS AS) - PROBLEM RECORD 436451   *00260000
000270*            BIJVOEGEN PARMDATE + TEST OP DA-CRE-EVENT-PROD      *00270000
000280*                                                                *00280000
000290* 12/03/97 : HEYSE K. (SOFT GUIDE)                               *00290000
000300*            AANPASSINGEN EURO EN 2000                           *00300000
000310*            UITBREIDEN BEDRAGEN                                 *00310000
000320*            UITBREIDEN JAARTAL TOT 4 POS VOOR 2000              *00320000
000330*                                                                *00330000
000340* 04/03/98 : DE SCHEPPER KOEN - PROJECT 5421 : TESTWAARDEN       *00340000
000350*            CI CREATIE MEE DOORGEVEN NAAR VERVOLG OM DE         *00350000
000360*            SPLITSING TEST-REEEL TE KUNNEN DOEN                 *00360000
000370* J-M BOOGAERTS                                                  *00370000
000380* 2004/12 REPRENDRE N° DE TITRE EN OUTPUT (12 POS DE LIBRES)     *00380000
000390*                                                                *00390000
000400*                                                                *00400000
000410******************************************************************00410000
000420/                                                                 00420000
000430 ENVIRONMENT DIVISION.                                            00430000
000440*---------------------                                            00440000
000450 INPUT-OUTPUT SECTION.                                            00450000
000460 FILE-CONTROL.                                                    00460000
000470     SELECT UITBST ASSIGN TO UT-S-DD005.                          00470000
000480/                                                                 00480000
000490 DATA DIVISION.                                                   00490000
000500*--------------                                                   00500000
000510 FILE SECTION.                                                    00510000
000520*                                                                 00520000
000530 FD  UITBST                                                       00530000
000540     BLOCK CONTAINS 0 RECORDS                                     00540000
000550     RECORD CONTAINS 50 CHARACTERS                                00550000
000560     RECORDING MODE F                                             00560000
000570     LABEL RECORDS STANDARD.                                      00570000
000580 01  UITRECORD.                                                   00580000
000590     03  UIT-AM-CN-STOCK          PIC S9(13)V99 COMP-3.           00590000
000600     03  UIT-AM-CND-STOCK         PIC S9(13)V99 COMP-3.           00600000
000610     03  UIT-NR-CIO-CRE           PIC 9(6).                       00610000
000620     03  UIT-NR-ID                PIC X(04).                      00620000
000630     03  UIT-NS-SEQ               PIC 9(04).                      00630000
000640     03  UIT-DA-UBSEC             PIC X(08).                      00640000
000650     03  UIT-NR-ST                PIC X(12).                      00650000
000660*                                                                 00660000
000670*                                                                 00670000
000680 WORKING-STORAGE SECTION.                                         00680000
000690*                                                                 00690000
000700 01  WS-TE-WORK.                                                  00700000
000710     10  WS-STATUS                PIC X    VALUE SPACE.           00710000
000720     10  SW-STATUS-D              PIC X    VALUE 'N'.             00720000
000730     10  USERABEN                 PIC X(8) VALUE 'USERABEN'.      00730000
000740     10  WS-NR-ID-GOOD.                                           00740000
000750         20  WS-NR-CIO-CRE        PIC 9(8) COMP-3.                00750000
000760         20  WS-DA-CR-CRE         PIC 9(8) COMP-3.                00760000
000770         20  WS-NR-ID-CRE         PIC 9(6) COMP-3.                00770000
000780         20  WS-CT-OPD-CRE        PIC S9(3) COMP-3.               00780000
000790         20  WS-CT-OPG-CRE        PIC 9(3) COMP-3.                00790000
000800         20  FILLER               PIC X(2).                       00800000
000810     10  CS-PROGRAM               PIC X(8)    VALUE 'VMDZ4420'.   00810000
000820     10  WS-NB-OUTPUT-COUNT       PIC 9(7)    COMP-3 VALUE ZEROES.00820000
000830     10  WS-NB-BEFF-COUNT         PIC 9(7)    COMP-3 VALUE ZEROES.00830000
000840*                                                                 00840000
000850*----- FIELDS ESDATMAS ------------------------------------------*00850000
000860     COPY ESDATMAS.                                               00860000
000870*----- FIELDS PARAMETER DATE ------------------------------------*00870000
000880 01  ZONE-DATONLY.                                                00880000
000890     03  DATE6R-WS.                                               00890000
000900         05  D-YEAR               PIC 99.                         00900000
000910         05  D-MONTH              PIC 99.                         00910000
000920         05  D-DAY                PIC 99.                         00920000
000930     03  DATE6 REDEFINES DATE6R-WS.                               00930000
000940         05  D-DAY                PIC 99.                         00940000
000950         05  D-MONTH              PIC 99.                         00950000
000960         05  D-YEAR               PIC 99.                         00960000
000970     03  DATE8.                                                   00970000
000980         05  D-DAY                PIC 99.                         00980000
000990         05  D-MONTH              PIC 99.                         00990000
001000         05  D-CENT               PIC 99.                         01000000
001010         05  D-YEAR               PIC 99.                         01010000
001020     03  PARMDATE.                                                01020000
001030         05  D-YEAR               PIC 9(4).                       01030000
001040         05  D-MONTH              PIC 9(2).                       01040000
001050         05  D-DAY                PIC 9(2).                       01050000
001060*                                                                 01060000
001070                                                                  01070000
001080     EXEC SQL INCLUDE SQLERRWS END-EXEC.                          01080000
001090     EXEC SQL INCLUDE SQLCA END-EXEC.                             01090000
001100     EXEC SQL INCLUDE DZBEFFTV END-EXEC.                          01100000
001110     EXEC SQL INCLUDE DZEVEFTV END-EXEC.                          01110000
001120                                                                  01120000
001130 01  WS-DZBEFFC1-FLAG               PIC X.                        01130000
001140     88  DZBEFFC1-NOT-EOC           VALUE 'N'.                    01140000
001150     88  DZBEFFC1-EOC               VALUE 'Y'.                    01150000
001160                                                                  01160000
001170 01  WS-DZEVEFC1-FLAG               PIC X.                        01170000
001180     88  DZEVEFC1-NOT-EOC           VALUE 'N'.                    01180000
001190     88  DZEVEFC1-EOC               VALUE 'Y'.                    01190000
001200                                                                  01200000
001210                                                                  01210000
001220     EXEC SQL DECLARE DZBEFFC1 CURSOR FOR                         01220000
001230       SELECT AM_CNDSTK_479BEFF                                   01230000
001240            , AM_CNSTK_479BEFF                                    01240000
001250            , CO_IDPRKSK_479BEFF                                  01250000
001260            , DA_UBSECIS_479BEFF                                  01260000
001270            , NR_IDSTOCK_479BEFF                                  01270000
001280            , NS_IRMOSTK_479BEFF                                  01280000
001290            , CT_RKTPROD_479BEFF                                  01290000
001300            , NR_CDSTK_479BEFF                                    01300000
001310            , NS_DBSTK_479BEFF                                    01310000
001320       FROM DZBEFFTV                                              01320000
001330       FOR READ ONLY                                              01330000
001340       QUERYNO 254                                                01340000
001350     END-EXEC                                                     01350000
001360                                                                  01360000
001370     EXEC SQL DECLARE DZEVEFC1 CURSOR FOR                         01370000
001380       SELECT CO_STEVPRN_479EVEF                                  01380000
001390            , CT_RKTEVPR_479EVEF                                  01390000
001400            , DA_CREVTPD_479EVEF                                  01400000
001410            , NR_IDGOOD_479EVEF                                   01410000
001420            , NR_ID_479EVEF                                       01420000
001430       FROM DZEVEFTV                                              01430000
001440       WHERE CT_RKTPROD_479BEFF = :DCLDZBEFFTV.CT-RKTPROD-479BEFF 01440000
001450         AND NR_IDSTOCK_479BEFF = :DCLDZBEFFTV.NR-IDSTOCK-479BEFF 01450000
001460         AND NR_CDSTK_479BEFF = :DCLDZBEFFTV.NR-CDSTK-479BEFF     01460000
001470         AND NS_DBSTK_479BEFF = :DCLDZBEFFTV.NS-DBSTK-479BEFF     01470000
001480       ORDER BY NR_ID_479EVEF DESC                                01480000
001490       FOR READ ONLY                                              01490000
001500       QUERYNO 255                                                01500000
001510     END-EXEC.                                                    01510000
001520                                                                  01520000
001530*DB2 DATE CONVERSION WORKING STORAGE                              01530000
001540 01  WS-DATUMVELDEN.                                              01540000
001550     03  DA-CCYYMMDD.                                             01550000
001560         05  CC                    PIC 99       VALUE ZERO.       01560000
001570         05  YY                    PIC 99       VALUE ZERO.       01570000
001580         05  MM                    PIC 99       VALUE ZERO.       01580000
001590         05  DD                    PIC 99       VALUE ZERO.       01590000
001600     03  DA-CCYYMMDD-R REDEFINES DA-CCYYMMDD.                     01600000
001610         05  CCYY                  PIC 9999.                      01610000
001620         05  MM                    PIC 99.                        01620000
001630         05  DD                    PIC 99.                        01630000
001640     03  DA-DD-MM-CCYY.                                           01640000
001650         05  DD                    PIC 9(02).                     01650000
001660         05  TE-MARKER5            PIC X        VALUE '.'.        01660000
001670         05  MM                    PIC 9(02).                     01670000
001680         05  TE-MARKER6            PIC X        VALUE '.'.        01680000
001690         05  CCYY                  PIC 9(04).                     01690000
001700     02  HELP-DA-CREVTPD-479EVEF        PIC 9(8)     VALUE ZEROES.01700000
001710                                                                  01710000
001720                                                                  01720000
001730 01  WS-TIMESTAMP-FIELDS.                                         01730000
001740     05 TS-SYSTEM.                                                01740000
001750        10  DA-SYS.                                               01750000
001760            15  DA-SYS-CCYY.                                      01760000
001770                20  CC            PIC X(2).                       01770000
001780                20  YY            PIC X(2).                       01780000
001790            15  MM                PIC X(2).                       01790000
001800            15  DD                PIC X(2).                       01800000
001810        10  HR-SYS.                                               01810000
001820            15  HH                PIC X(2).                       01820000
001830            15  MI                PIC X(2).                       01830000
001840            15  SS                PIC X(2).                       01840000
001850            15  TT                PIC X(2).                       01850000
001860     05 TS-TIMESTAMP.                                             01860000
001870        10  CC                    PIC X(2).                       01870000
001880        10  YY                    PIC X(2).                       01880000
001890        10  TE-MARKER1            PIC X             VALUE '-'.    01890000
001900        10  MM                    PIC X(2).                       01900000
001910        10  TE-MARKER2            PIC X             VALUE '-'.    01910000
001920        10  DD                    PIC X(2).                       01920000
001930        10  TE-MARKER3            PIC X             VALUE '-'.    01930000
001940        10  HH                    PIC X(2).                       01940000
001950        10  TE-MARKER4            PIC X             VALUE '.'.    01950000
001960        10  MI                    PIC X(2).                       01960000
001970        10  TE-MARKER5            PIC X             VALUE '.'.    01970000
001980        10  SS                    PIC X(2).                       01980000
001990        10  TE-MARKER6            PIC X             VALUE '.'.    01990000
002000        10  TT                    PIC X(2).                       02000000
002010        10  NNNN                  PIC 9(04)         VALUE 0.      02010000
002020                                                                  02020000
002030 LINKAGE SECTION.                                                 02030000
002040 01  PARAM-DATONLY.                                               02040000
002050     03  L-PARAM                  PIC S9(4) COMP.                 02050000
002060     03  DATUMLS.                                                 02060000
002070         05  DATE-IND             PIC X.                          02070000
002080         05  DATE8-LS             PIC X(8).                       02080000
002090     EJECT                                                        02090000
002100 PROCEDURE DIVISION USING PARAM-DATONLY.                          02100000
002110*                                                                 02110000
002120* INITIALISATIE                                                   02120000
002130*                                                                 02130000
002140     PERFORM 600-GET-TIMESTAMP.                                   02140000
002150     IF DATE-IND = '0'                                            02150000
002160        ACCEPT DATE6R-WS FROM DATE                                02160000
002170        MOVE CORR DATE6R-WS TO DATE8                              02170000
002180        IF D-YEAR OF DATE8 > 60                                   02180000
002190           MOVE 19 TO D-CENT OF DATE8                             02190000
002200        ELSE MOVE 20 TO D-CENT OF DATE8                           02200000
002210        END-IF                                                    02210000
002220        MOVE CORR DATE8 TO DATE6                                  02220000
002230     ELSE                                                         02230000
002240        MOVE DATE8-LS   TO DATE8                                  02240000
002250        MOVE CORR DATE8 TO DATE6                                  02250000
002260     END-IF.                                                      02260000
002270     MOVE DATE6 TO ES-DATUM.                                      02270000
002280     MOVE ZEROES TO ES-DAGEN,                                     02280000
002290                    ES-TYPE-DAG.                                  02290000
002300     MOVE '+' TO ES-PLUS-MIN.                                     02300000
002310*                                                                 02310000
002320     CALL ESDATMAS USING ES-DATUM ES-DAGEN ES-TYPE-DAG ES-PLUS-MIN02320000
002330     ES-ANTWOORD ES-RETURN-CODE ES-WERKZONE.                      02330000
002340*                                                                 02340000
002350     IF ES-RETURN-CODE = '0'                                      02350000
002360        MOVE ES-JJJJ TO D-YEAR OF PARMDATE                        02360000
002370        MOVE ES-MM   TO D-MONTH OF PARMDATE                       02370000
002380        MOVE ES-DD   TO D-DAY OF PARMDATE                         02380000
002390     ELSE DISPLAY '***********************************'           02390000
002400        DISPLAY ' '                                               02400000
002410        DISPLAY 'PARAMETER DATE IN ERROR = ' DATE6                02410000
002420        DISPLAY ' '                                               02420000
002430        DISPLAY '***********************************'             02430000
002440        CALL USERABEN                                             02440000
002450     END-IF.                                                      02450000
002460*                                                                 02460000
002470     MOVE CS-PROGRAM TO PROGRAM-NAME.                             02470000
002480     OPEN OUTPUT UITBST.                                          02480000
002490                                                                  02490000
002500     INITIALIZE DCLDZBEFFTV                                       02500000
002510     PERFORM 2100-OPEN-DZBEFFC1.                                  02510000
002520     PERFORM 2200-FETCH-DZBEFFC1 UNTIL DZBEFFC1-EOC.              02520000
002530     PERFORM 2300-CLOSE-DZBEFFC1.                                 02530000
002540*                                                                 02540000
002550* HOOFDVERWERKING                                                 02550000
002560*                                                                 02560000
002570*                                                                 02570000
002580* EINDVERWERKING                                                  02580000
002590*                                                                 02590000
002600     CLOSE UITBST.                                                02600000
002610     DISPLAY 'TOTAL BEFF RECORDS   : ' WS-NB-BEFF-COUNT           02610000
002620     DISPLAY 'TOTAL OUTPUT RECORDS : ' WS-NB-OUTPUT-COUNT         02620000
002630                                                                  02630000
002640     STOP RUN.                                                    02640000
002650/                                                                 02650000
002660 HOOFDVERWERKING.                                                 02660000
002670*                                                                 02670000
002680* OPZOEKEN VAN ALLE EVENEMENTEN BIJ EEN EFFECT                    02680000
002690*                                                                 02690000
002700     MOVE SPACE TO WS-STATUS                                      02700000
002710     INITIALIZE DCLDZEVEFTV                                       02710000
002720     PERFORM 3100-OPEN-DZEVEFC1                                   02720000
002730     MOVE 'N' TO SW-STATUS-D                                      02730000
002740     PERFORM 3200-FETCH-DZEVEFC1 UNTIL DZEVEFC1-EOC OR            02740000
002750                                  SW-STATUS-D = 'Y'               02750000
002760     PERFORM 3300-CLOSE-DZEVEFC1.                                 02760000
002770                                                                  02770000
002780     IF NOT SW-STATUS-D = 'Y'                                     02780000
002790        IF WS-STATUS = 'C'                                        02790000
002800           PERFORM WRITE-UITRECORD                                02800000
002810           ADD 1 TO WS-NB-OUTPUT-COUNT                            02810000
002820        END-IF                                                    02820000
002830     END-IF.                                                      02830000
002840*                                                                 02840000
002850* OPZOEKEN VAN VOLGEND EFFECT IN DE AREA                          02850000
002860*                                                                 02860000
002870*                                                                 02870000
002880                                                                  02880000
002890/                                                                 02890000
002900 WRITE-UITRECORD.                                                 02900000
002910     INITIALIZE UITRECORD                                         02910000
002920     MOVE AM-CNSTK-479BEFF OF DCLDZBEFFTV   TO UIT-AM-CN-STOCK    02920000
002930     MOVE AM-CNDSTK-479BEFF OF DCLDZBEFFTV  TO UIT-AM-CND-STOCK   02930000
002940     MOVE WS-NR-CIO-CRE                     TO UIT-NR-CIO-CRE     02940000
002950     MOVE CO-IDPRKSK-479BEFF OF DCLDZBEFFTV TO UIT-NR-ID          02950000
002960     MOVE NS-IRMOSTK-479BEFF OF DCLDZBEFFTV TO UIT-NS-SEQ         02960000
002970     MOVE ZEROES                            TO DA-CCYYMMDD        02970000
002980     MOVE DA-UBSECIS-479BEFF OF DCLDZBEFFTV TO DA-DD-MM-CCYY      02980000
002990     EVALUATE TRUE                                                02990000
003000       WHEN DA-DD-MM-CCYY = '01.01.0001'                          03000000
003010            MOVE ZEROES                TO DA-CCYYMMDD-R           03010000
003020       WHEN DA-DD-MM-CCYY = '31.12.9999'                          03020000
003030            MOVE '99999999'            TO DA-CCYYMMDD-R           03030000
003040       WHEN OTHER                                                 03040000
003050            MOVE CCYY OF DA-DD-MM-CCYY TO CCYY OF DA-CCYYMMDD-R   03050000
003060            MOVE MM   OF DA-DD-MM-CCYY TO MM OF DA-CCYYMMDD-R     03060000
003070            MOVE DD   OF DA-DD-MM-CCYY TO DD OF DA-CCYYMMDD-R     03070000
003080     END-EVALUATE                                                 03080000
003090     MOVE DA-CCYYMMDD-R                     TO UIT-DA-UBSEC       03090000
003100     MOVE NR-IDSTOCK-479BEFF OF DCLDZBEFFTV TO UIT-NR-ST          03100000
003110     WRITE UITRECORD.                                             03110000
003120                                                                  03120000
003130 VERWERK-VMBEVEF.                                                 03130000
003140     MOVE ZEROES TO DA-CCYYMMDD                                   03140000
003150     MOVE ZEROES TO HELP-DA-CREVTPD-479EVEF                       03150000
003160     MOVE DA-CREVTPD-479EVEF OF DCLDZEVEFTV TO DA-DD-MM-CCYY      03160000
003170     EVALUATE TRUE                                                03170000
003180       WHEN DA-DD-MM-CCYY = '01.01.0001'                          03180000
003190            MOVE ZEROES                TO DA-CCYYMMDD-R           03190000
003200       WHEN DA-DD-MM-CCYY = '31.12.9999'                          03200000
003210            MOVE '99999999'            TO DA-CCYYMMDD-R           03210000
003220       WHEN OTHER                                                 03220000
003230            MOVE CCYY OF DA-DD-MM-CCYY TO CCYY OF DA-CCYYMMDD-R   03230000
003240            MOVE MM   OF DA-DD-MM-CCYY TO MM OF DA-CCYYMMDD-R     03240000
003250            MOVE DD   OF DA-DD-MM-CCYY TO DD OF DA-CCYYMMDD-R     03250000
003260     END-EVALUATE                                                 03260000
003270     MOVE DA-CCYYMMDD-R TO HELP-DA-CREVTPD-479EVEF                03270000
003280     IF HELP-DA-CREVTPD-479EVEF NOT > PARMDATE                    03280000
003290        IF CT-RKTEVPR-479EVEF OF DCLDZEVEFTV = '0060' AND         03290000
003300             WS-STATUS NOT = 'D'                                  03300000
003310           MOVE 'C'                              TO WS-STATUS     03310000
003320           MOVE NR-IDGOOD-479EVEF OF DCLDZEVEFTV TO WS-NR-ID-GOOD 03320000
003330        ELSE                                                      03330000
003340           IF CT-RKTEVPR-479EVEF OF DCLDZEVEFTV = '0168' AND      03340000
003350                  CO-STEVPRN-479EVEF OF DCLDZEVEFTV NOT = '1'     03350000
003360              MOVE 'D' TO WS-STATUS                               03360000
003370              MOVE 'Y' TO SW-STATUS-D                             03370000
003380           ELSE                                                   03380000
003390              IF CT-RKTEVPR-479EVEF OF DCLDZEVEFTV = '0217'       03390000
003400                      AND WS-STATUS = SPACE                       03400000
003410                 MOVE 'S' TO WS-STATUS                            03410000
003420              END-IF                                              03420000
003430           END-IF                                                 03430000
003440        END-IF                                                    03440000
003450     END-IF.                                                      03450000
003460/                                                                 03460000
003470                                                                  03470000
003480                                                                  03480000
003490 2100-OPEN-DZBEFFC1.                                              03490000
003500D    DISPLAY '2100-OPEN-DZBEFFC1.'                                03500000
003510     MOVE 2100 TO SQL-LOCATION                                    03510000
003520                                                                  03520000
003530     EXEC SQL                                                     03530000
003540       OPEN DZBEFFC1                                              03540000
003550     END-EXEC                                                     03550000
003560                                                                  03560000
003570     EVALUATE SQLCODE                                             03570000
003580       WHEN ZERO                                                  03580000
003590            SET DZBEFFC1-NOT-EOC TO TRUE                          03590000
003600       WHEN OTHER                                                 03600000
003610            DISPLAY 'ERROR WHILE OPENING CURSOR DZBEFFC1'         03610000
003620            PERFORM SQLERROR                                      03620000
003630     END-EVALUATE                                                 03630000
003640     .                                                            03640000
003650                                                                  03650000
003660 2200-FETCH-DZBEFFC1.                                             03660000
003670D    DISPLAY '2200-FETCH-DZBEFFC1.'                               03670000
003680     SET DZBEFFC1-NOT-EOC TO TRUE                                 03680000
003690     MOVE 2200 TO SQL-LOCATION                                    03690000
003700                                                                  03700000
003710     EXEC SQL                                                     03710000
003720       FETCH DZBEFFC1                                             03720000
003730        INTO :DCLDZBEFFTV.AM-CNDSTK-479BEFF                       03730000
003740           , :DCLDZBEFFTV.AM-CNSTK-479BEFF                        03740000
003750           , :DCLDZBEFFTV.CO-IDPRKSK-479BEFF                      03750000
003760           , :DCLDZBEFFTV.DA-UBSECIS-479BEFF                      03760000
003770           , :DCLDZBEFFTV.NR-IDSTOCK-479BEFF                      03770000
003780           , :DCLDZBEFFTV.NS-IRMOSTK-479BEFF                      03780000
003790           , :DCLDZBEFFTV.CT-RKTPROD-479BEFF                      03790000
003800           , :DCLDZBEFFTV.NR-CDSTK-479BEFF                        03800000
003810           , :DCLDZBEFFTV.NS-DBSTK-479BEFF                        03810000
003820     END-EXEC                                                     03820000
003830                                                                  03830000
003840     EVALUATE SQLCODE                                             03840000
003850       WHEN ZERO                                                  03850000
003860            ADD 1 TO WS-NB-BEFF-COUNT                             03860000
003870            PERFORM HOOFDVERWERKING                               03870000
003880       WHEN 100                                                   03880000
003890            SET DZBEFFC1-EOC TO TRUE                              03890000
003900       WHEN OTHER                                                 03900000
003910            DISPLAY 'ERROR WHILE FETCHING CURSOR DZBEFFC1'        03910000
003920            PERFORM SQLERROR                                      03920000
003930     END-EVALUATE                                                 03930000
003940     .                                                            03940000
003950                                                                  03950000
003960 2300-CLOSE-DZBEFFC1.                                             03960000
003970D    DISPLAY '2300-CLOSE-DZBEFFC1.'                               03970000
003980     MOVE 2300 TO SQL-LOCATION                                    03980000
003990                                                                  03990000
004000     EXEC SQL                                                     04000000
004010       CLOSE DZBEFFC1                                             04010000
004020     END-EXEC                                                     04020000
004030                                                                  04030000
004040     EVALUATE SQLCODE                                             04040000
004050       WHEN ZERO                                                  04050000
004060            CONTINUE                                              04060000
004070       WHEN OTHER                                                 04070000
004080            DISPLAY 'ERROR WHILE CLOSING CURSOR DZBEFFC1'         04080000
004090            PERFORM SQLERROR                                      04090000
004100     END-EVALUATE                                                 04100000
004110     .                                                            04110000
004120                                                                  04120000
004130 3100-OPEN-DZEVEFC1.                                              04130000
004140D    DISPLAY '3100-OPEN-DZEVEFC1.'                                04140000
004150     MOVE 3100 TO SQL-LOCATION                                    04150000
004160                                                                  04160000
004170     EXEC SQL                                                     04170000
004180       OPEN DZEVEFC1                                              04180000
004190     END-EXEC                                                     04190000
004200                                                                  04200000
004210     EVALUATE SQLCODE                                             04210000
004220       WHEN ZERO                                                  04220000
004230            SET DZEVEFC1-NOT-EOC TO TRUE                          04230000
004240       WHEN OTHER                                                 04240000
004250            DISPLAY 'ERROR WHILE OPENING CURSOR DZEVEFC1'         04250000
004260            PERFORM SQLERROR                                      04260000
004270     END-EVALUATE                                                 04270000
004280     .                                                            04280000
004290                                                                  04290000
004300 3200-FETCH-DZEVEFC1.                                             04300000
004310D    DISPLAY '3200-FETCH-DZEVEFC1.'                               04310000
004320     SET DZEVEFC1-NOT-EOC TO TRUE                                 04320000
004330     MOVE 3200 TO SQL-LOCATION                                    04330000
004340                                                                  04340000
004350     EXEC SQL                                                     04350000
004360       FETCH DZEVEFC1                                             04360000
004370        INTO :DCLDZEVEFTV.CO-STEVPRN-479EVEF                      04370000
004380           , :DCLDZEVEFTV.CT-RKTEVPR-479EVEF                      04380000
004390           , :DCLDZEVEFTV.DA-CREVTPD-479EVEF                      04390000
004400           , :DCLDZEVEFTV.NR-IDGOOD-479EVEF                       04400000
004410           , :DCLDZEVEFTV.NR-ID-479EVEF                           04410000
004420     END-EXEC                                                     04420000
004430                                                                  04430000
004440     EVALUATE SQLCODE                                             04440000
004450       WHEN ZERO                                                  04450000
004460            PERFORM VERWERK-VMBEVEF                               04460000
004470       WHEN 100                                                   04470000
004480            SET DZEVEFC1-EOC TO TRUE                              04480000
004490       WHEN OTHER                                                 04490000
004500            DISPLAY 'ERROR WHILE FETCHING CURSOR DZEVEFC1'        04500000
004510            DISPLAY 'CT-RK-TPROD    = ' CT-RKTPROD-479BEFF        04510000
004520                                        OF DCLDZBEFFTV            04520000
004530            DISPLAY 'NR-ID-STOCK-R1 = ' NR-IDSTOCK-479BEFF        04530000
004540                                        OF DCLDZBEFFTV            04540000
004550            DISPLAY 'NR-CD-STOCK    = ' NR-CDSTK-479BEFF          04550000
004560                                        OF DCLDZBEFFTV            04560000
004570            DISPLAY 'NS-DB-STOCK    = ' NS-DBSTK-479BEFF          04570000
004580                                        OF DCLDZBEFFTV            04580000
004590            PERFORM SQLERROR                                      04590000
004600     END-EVALUATE                                                 04600000
004610     .                                                            04610000
004620                                                                  04620000
004630 3300-CLOSE-DZEVEFC1.                                             04630000
004640D    DISPLAY '3300-CLOSE-DZEVEFC1.'                               04640000
004650     MOVE 3300 TO SQL-LOCATION                                    04650000
004660                                                                  04660000
004670     EXEC SQL                                                     04670000
004680       CLOSE DZEVEFC1                                             04680000
004690     END-EXEC                                                     04690000
004700                                                                  04700000
004710     EVALUATE SQLCODE                                             04710000
004720       WHEN ZERO                                                  04720000
004730            CONTINUE                                              04730000
004740       WHEN OTHER                                                 04740000
004750            DISPLAY 'ERROR WHILE CLOSING CURSOR DZEVEFC1'         04750000
004760            PERFORM SQLERROR                                      04760000
004770     END-EVALUATE                                                 04770000
004780     .                                                            04780000
004790                                                                  04790000
004800                                                                  04800000
004810 600-GET-TIMESTAMP.                                               04810000
004820D    DISPLAY '600-GET-TIMESTAMP.'                                 04820000
004830     MOVE FUNCTION CURRENT-DATE TO TS-SYSTEM.                     04830000
004840     MOVE CC OF TS-SYSTEM       TO CC OF TS-TIMESTAMP             04840000
004850     MOVE YY OF TS-SYSTEM       TO YY OF TS-TIMESTAMP             04850000
004860     MOVE MM OF TS-SYSTEM       TO MM OF TS-TIMESTAMP             04860000
004870     MOVE DD OF TS-SYSTEM       TO DD OF TS-TIMESTAMP             04870000
004880     MOVE HH OF TS-SYSTEM       TO HH OF TS-TIMESTAMP             04880000
004890     MOVE MI OF TS-SYSTEM       TO MI OF TS-TIMESTAMP             04890000
004900     MOVE SS OF TS-SYSTEM       TO SS OF TS-TIMESTAMP             04900000
004910     MOVE TT OF TS-SYSTEM       TO TT OF TS-TIMESTAMP             04910000
004920     DISPLAY 'TIMESTAMP: ' TS-TIMESTAMP                           04920000
004930     .                                                            04930000
004940                                                                  04940000
004950*SQLERROR ROUTINE.                                                04950000
004960     EXEC SQL                                                     04960000
004970          INCLUDE SQLERROR                                        04970000
004980     END-EXEC.                                                    04980000
