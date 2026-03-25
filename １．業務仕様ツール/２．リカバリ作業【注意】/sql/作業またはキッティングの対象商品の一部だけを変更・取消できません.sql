SET ECHO ON
select 'B' || SUBSTR(CR_NUM,2,14) "★ダミー受注番号★" from TJFAX151_CUSTOMER_REQUEST where inquiry_num ='【置換文字列1】';

SELECT CR_NUM||','||CR_L_NUM||','||CR_LINE_HIST_NUM||','||CR_SERVICE_L_NUM||','||OBJECT_OF_SERVICE_ITEM_CD||','||OBJ_SERV_ITEM_NAME||','||L_FLG FROM TJFAX15H_CR_SERVICE_ITEM
  WHERE CR_NUM = (select cr_num from TJFAX151_CUSTOMER_REQUEST where inquiry_num ='【置換文字列1】')
    and OBJECT_OF_SERVICE_ITEM_CD='【置換文字列2】'
;

UPDATE TJFAX15H_CR_SERVICE_ITEM
 SET CR_NUM=(SELECT 'B'||SUBSTR(cr_num,2,14) from TJFAX151_CUSTOMER_REQUEST where inquiry_num ='【置換文字列1】')
  WHERE CR_NUM = (select cr_num from TJFAX151_CUSTOMER_REQUEST where inquiry_num ='【置換文字列1】')
    AND OBJECT_OF_SERVICE_ITEM_CD='【置換文字列2】'
    AND L_FLG='1'
;

SELECT CR_NUM||','||CR_L_NUM||','||CR_LINE_HIST_NUM||','||CR_SERVICE_L_NUM||','||OBJECT_OF_SERVICE_ITEM_CD||','||OBJ_SERV_ITEM_NAME||','||L_FLG FROM TJFAX15H_CR_SERVICE_ITEM
  WHERE CR_NUM = (select 'B'||SUBSTR(cr_num,2,14) from TJFAX151_CUSTOMER_REQUEST where inquiry_num ='【置換文字列1】')
    and OBJECT_OF_SERVICE_ITEM_CD='【置換文字列2】'
;

SELECT CR_NUM,CR_L_NUM,CR_LINE_HIST_NUM,CR_ITEM_CD,ASSORT_NUM,L_FLG FROM TJFAX15A_CR_ITEM
 WHERE inquiry_num ='【置換文字列1】' AND CR_ITEM_CD='【置換文字列2】' AND L_FLG='1';

--▼セット化解除（もし必要があれば）
--UPDATE TJFAX15A_CR_ITEM SET ASSORT_NUM='0' WHERE inquiry_num ='&1' AND CR_ITEM_CD='&2' AND L_FLG='1';

SELECT CR_ITEM_CD||'('||CR_ITEM_NAME||')を削除できるようにメンテナンスしました。再度取消操作をお願いいたします。' FROM TJFAX15A_CR_ITEM
  WHERE  inquiry_num ='【置換文字列1】' AND CR_ITEM_CD='【置換文字列2】' AND L_FLG='1';

--commit;
