--(参考)INC2025071700157 配送予約のキャンセルデータが連携されない？
set echo on

--確認
select TO_CHAR(SYSdate,'yyyy/mm/dd hh24:mi:ss')  AS "現在日時" from dual;
select distinct inquiry_num,substr(inquiry_num,3,8),EARLY_DVLRY_RESERVE_NUM,EARLY_DVLRY_RESERVE_DATE from TJFAX15A_CR_ITEM where inquiry_num='JS' || '【置換文字列1】'||'1' and EARLY_DVLRY_RESERVE_NUM is not null;


select * from TJFAX15O_DELI_RESERVE_MGMT where DELI_RESERVE_MGMT_NUM in ('【置換文字列1】');
Insert into TJFAX15O_DELI_RESERVE_MGMT values ('【置換文字列2】','【置換文字列1】',null,sysdate,sysdate,'90','1','0',null,'★日付★',null,null,'1',sysdate,'p000h12834',sysdate,'p000h12834');
select * from TJFAX15O_DELI_RESERVE_MGMT where DELI_RESERVE_MGMT_NUM in ('【置換文字列1】');

--commit;
