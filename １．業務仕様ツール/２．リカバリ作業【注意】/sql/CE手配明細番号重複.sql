--¡ì‹Æ‚r‚p‚k
set echo on
--¥Šm”F
select TO_CHAR(SYSdate,'yyyy/mm/dd hh24:mi:ss')  AS "Œ»İ“ú" from dual;
--¥–â‡‚¹–¾×”Ô†‚ªd•¡‚µ‚Ä‚¢‚é–¾×‚ğŠm”F
select INQUIRY_L_NUM,count(*) from TJFAX15A_CR_ITEM where inquiry_num ='y’uŠ·•¶š—ñ1z' and l_flg='1' having count(*)>1 group by INQUIRY_L_NUM;
select cr_num,INQUIRY_L_NUM,cr_l_num from TJFAX15A_CR_ITEM where inquiry_num ='y’uŠ·•¶š—ñ1z' and INQUIRY_L_NUM in (select INQUIRY_L_NUM from (select INQUIRY_L_NUM,count(*) from TJFAX15A_CR_ITEM where inquiry_num ='y’uŠ·•¶š—ñ1z' and l_flg='1'  having count(*)>1 group by INQUIRY_L_NUM))  order by INQUIRY_L_NUM asc,CR_L_NUM asc;
select cr_num,INQUIRY_L_NUM,cr_l_num from TJFAX371_SVC_ARR where inquiry_num ='y’uŠ·•¶š—ñ1z' and INQUIRY_L_NUM in (select INQUIRY_L_NUM from (select INQUIRY_L_NUM,count(*) from TJFAX15A_CR_ITEM where inquiry_num ='y’uŠ·•¶š—ñ1z' and l_flg='1'  having count(*)>1 group by INQUIRY_L_NUM))  order by INQUIRY_L_NUM asc,CR_L_NUM asc;

--¥ó’¤•i–¾×
update TJFAX15A_CR_ITEM set inquiry_l_num = '9'||substr(inquiry_l_num,2,4),last_updated_by_id = 'p000h12834',last_update_datetime = sysdate where INQUIRY_NUM = 'y’uŠ·•¶š—ñ1z' and inquiry_l_num = '81635' and cr_l_num = 572;
update TJFAX15A_CR_ITEM set inquiry_l_num = '9'||substr(inquiry_l_num,2,4),last_updated_by_id = 'p000h12834',last_update_datetime = sysdate where INQUIRY_NUM = 'y’uŠ·•¶š—ñ1z' and inquiry_l_num = '81636' and cr_l_num = 573;

--¥–ğ–±è”z
update TJFAX371_SVC_ARR set inquiry_l_num = '9'||substr(inquiry_l_num,2,4),last_updated_by_id = 'p000h12834',last_update_datetime = sysdate where INQUIRY_NUM = 'y’uŠ·•¶š—ñ1z' and inquiry_l_num = '81636' and cr_l_num = 573;


--commit;


