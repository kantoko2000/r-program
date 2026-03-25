--実行したSQL文を表示しない
SET ECHO on 
SET PAGES 0
set pages 200 colsep,
SET LINESIZE  2000 COLSEP,
SET SERVEROUTPUT ON
--変数表示しない
SET VERIFY OFF
set heading On


SELECT DISTINCT
    a1.address_cd
    || ','
    || a1.住所名
    || ','
    || c.dist_base_cd "住所コード-住所名-物流拠点コード"
FROM
    (
        SELECT
            a.address_cd,
            a.prefectures_name
            || a.muni_name
            || a.oaza_alias_name
            || a.azana_name_cho AS 住所名
        FROM
            tjfxx02d_addr_m a
        WHERE
            a.prefectures_name
            || a.muni_name
            || a.oaza_alias_name
            || a.azana_name_cho LIKE '%&1%'
            AND address_invalid_flg = '0'
    )                         a1,
    tjfxx02k_address_area_m   b,
    tjfax643_dist_base_judg_m c
WHERE
    b.address_cd = a1.address_cd
    AND b.area_cd = c.area_cd
    AND c.deli_serv_ctgr NOT IN ( '16' );

--INSERT INTO TJFTX073_FFM_MULTI_PURPOSE VALUES ('0038','★トラン郵便番号★','★正しい住所コード★','★トラン_搬出届先住所１～３★','チェック済','','','','','','','','','','','','p000h12834',SYSDATE);


exit;
