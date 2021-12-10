--CBS202109_结算模块_优化六期 2021-11-17

--导入请求
DELETE FROM FMDBRUN.SFREQDEF WHERE REQTID IN ('APCNVQRY','PMVERIFY','APPERSAV','APPERQRY','PMPAYUPD');
IMPORT FROM 'SFREQDEF.del' of del COMMITCOUNT 1000 INSERT INTO  FMDBRUN.SFREQDEF;
DELETE FROM FMDBRUN.SFREQITF WHERE REQTID IN ('APCNVQRY','PMVERIFY','APPERSAV','APPERQRY','PMPAYUPD');
IMPORT FROM 'SFREQITF.del' of del COMMITCOUNT 1000 INSERT INTO  FMDBRUN.SFREQITF;
DELETE FROM FMDBRUN.SFITFDEF WHERE ITFCID IN (SELECT ITFCID  FROM FMDBRUN.SFREQITF WHERE REQTID IN ('APCNVQRY','PMVERIFY','APPERSAV','APPERQRY','PMPAYUPD'));
IMPORT FROM 'SFITFDEF.del' of del COMMITCOUNT 1000 INSERT INTO  FMDBRUN.SFITFDEF;
DELETE FROM FMDBRUN.SFITFFLD WHERE ITFCID IN (SELECT ITFCID  FROM FMDBRUN.SFREQITF WHERE REQTID IN ('APCNVQRY','PMVERIFY','APPERSAV','APPERQRY','PMPAYUPD'));
IMPORT FROM 'SFITFFLD.del' of del COMMITCOUNT 1000 INSERT INTO  FMDBRUN.SFITFFLD;
DELETE FROM FMDBRUN.SFREQPRJ WHERE REQTID IN ('APCNVQRY','PMVERIFY','APPERSAV','APPERQRY','PMPAYUPD');
IMPORT FROM 'SFREQPRJ.del' of del COMMITCOUNT 1000 INSERT INTO  FMDBRUN.SFREQPRJ;
DELETE FROM FMDBRUN.SFITFCFGP WHERE SICITFUID IN ('APCNVQRY','PMVERIFY','APPERSAV','APPERQRY','PMPAYUPD');
IMPORT FROM 'SFITFCFGP.del' of del COMMITCOUNT 1000 INSERT INTO  FMDBRUN.SFITFCFGP;
DELETE FROM FMDBRUN.SFBIZCFGP WHERE SBCCMDCOD IN ('RQAPCNVQRY','RQPMVERIFY','RQAPPERSAV','RQAPPERQRY','RQPMPAYUPD');
IMPORT FROM 'SFBIZCFGP.del' of del COMMITCOUNT 1000 INSERT INTO  FMDBRUN.SFBIZCFGP;
--导入接口
DELETE FROM FMDBRUN.SFITFDEF WHERE ITFCID IN ('ACACTINFX','ACACTINFY','APAGTQRYZ','PMPAYINFZ','PMPAYQRYX','PMVERIFYX','PMVERIFYZ','APPERUSRX','APPERTYPX','APPERQRYX','APPERQRYZ','PMMAIINFX','PMRESULTZ','PMOFFSAVX','PMOFFPAYZ','DCACINFOZ','APPAYSAVX','APPAYSAVZ');
IMPORT FROM 'SFITFDEF-other.del' of del COMMITCOUNT 1000 INSERT INTO  FMDBRUN.SFITFDEF;
DELETE FROM FMDBRUN.SFITFFLD WHERE ITFCID IN ('ACACTINFX','ACACTINFY','APAGTQRYZ','PMPAYINFZ','PMPAYQRYX','PMVERIFYX','PMVERIFYZ','APPERUSRX','APPERTYPX','APPERQRYX','APPERQRYZ','PMMAIINFX','PMRESULTZ','PMOFFSAVX','PMOFFPAYZ','DCACINFOZ','APPAYSAVX','APPAYSAVZ');
IMPORT FROM 'SFITFFLD-other.del' of del COMMITCOUNT 1000 INSERT INTO FMDBRUN.SFITFFLD;
--导入错误代码
DELETE FROM FMDBRUN.SFERRMSG WHERE ERRMSGKEY IN ('APSAL72','APPSI01','APPCK09','APPSI02','PMCHE32','APPCK09','PMCHE30','PMCHE31','APACP26','APPOC01','APPOC02','APSAL73','APPCK10','APSAL74');
IMPORT FROM 'SFERRMSG.del' of del COMMITCOUNT 1000 INSERT INTO FMDBRUN.SFERRMSG;



--请求
--'APCNVQRY','PMVERIFY','APPERSAV','APPERQRY','PMPAYUPD'
--接口
--'ACACTINFX','ACACTINFY','APAGTQRYZ','PMPAYINFZ','PMPAYQRYX','PMVERIFYX','PMVERIFYZ','APPERUSRX','APPERTYPX','APPERQRYX','APPERQRYZ','PMMAIINFX','PMRESULTZ','PMOFFSAVX','PMOFFPAYZ','DCACINFOZ','APPAYSAVX','APPAYSAVZ'
--错误代码
--'APSAL72','APPSI01','APPCK09','APPSI02','PMCHE32','APPCK09','PMCHE30','PMCHE31','APACP26','APPOC01','APPOC02','APSAL73','APPCK10','APSAL74'

