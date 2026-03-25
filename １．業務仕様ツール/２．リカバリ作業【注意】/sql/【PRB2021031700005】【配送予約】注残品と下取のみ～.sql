--ÅöÇP

--î¿ì¸ÅÀà⁄ìÆ

--âÊñ Ç≈ó\ñÒÇéÊÇËíºÇµ(ç°âÒïsóv)
SET ECHO ON
--Å•ÇPÅDéÛíçè§ïiñæç◊ÇÃçXêV
select cr_num,cr_l_num,cr_line_hist_num,inquiry_num,to_char(deadline,'YY-MM-DD HH24:MI:SS') deadline,fixed_after_shipping_date,fixed_after_ds_date,LINE_ALLOC_RESULT_CTGR,REQ_CARRY_IN_DATE,REQ_CARRY_OUT_DATE,EARLY_DVLRY_RESERVE_NUM,to_char(EARLY_DELI_RESV_GET_DT,'YY-MM-DD HH24:MI:SS') EARLY_DELI_RESV_GET_DT,EARLY_DVLRY_RESERVE_DATE,EARLY_DVLRY_RESERVE_TIME from tjfax15a_cr_item a
where inquiry_num = 'Åyíuä∑ï∂éöóÒ1Åz' and l_flg = '1' and cancel_flg = '0' order by cr_l_num;

update tjfax15a_cr_item
set
    --REQ_CARRY_IN_DATE  = '20240322',
    --REQ_CARRY_OUT_DATE = '20240322',
    --REQ_CARRY_IN_TIME_ZONE_CTGR = null,
    EARLY_DVLRY_RESERVE_NUM = '500002724',
    EARLY_DELI_RESV_GET_DT = '2024/03/15 16:41:03',
    EARLY_DVLRY_RESERVE_DATE = '20240322',
    EARLY_DVLRY_RESERVE_TIME = '07000830',
    last_updated_by_id = 'g10012013',
    last_update_datetime = sysdate
WHERE
        inquiry_num = 'Åyíuä∑ï∂éöóÒ1Åz'
    AND
		cr_l_num in (Åyíuä∑ï∂éöóÒ2Åz)
    AND
        l_flg = '1'
    AND
        cancel_flg = '0'
;

select cr_num,cr_l_num,cr_line_hist_num,inquiry_num,to_char(deadline,'YY-MM-DD HH24:MI:SS') deadline,fixed_after_shipping_date,fixed_after_ds_date,LINE_ALLOC_RESULT_CTGR,REQ_CARRY_IN_DATE,REQ_CARRY_OUT_DATE,EARLY_DVLRY_RESERVE_NUM,to_char(EARLY_DELI_RESV_GET_DT,'YY-MM-DD HH24:MI:SS') EARLY_DELI_RESV_GET_DT,EARLY_DVLRY_RESERVE_DATE,EARLY_DVLRY_RESERVE_TIME from tjfax15a_cr_item a
where inquiry_num = 'Åyíuä∑ï∂éöóÒ1Åz' and l_flg = '1' and cancel_flg = '0' order by cr_l_num;




--Å•ÇQÅDéÛíçî¿ì¸èoñæç◊ÇÃçXêV
select cr_num,DELIVERY_REQ_NUM,CUST_DEM_CR_IN_DATE,CUST_DEM_CR_OUT_DATE from tjfax157_cr_deliv a
where cr_num = 'Åyíuä∑ï∂éöóÒ3Åz';

update tjfax157_cr_deliv
set
    CUST_DEM_CR_IN_DATE = '20240322'
where
        cr_num = 'Åyíuä∑ï∂éöóÒ3Åz'
    AND
        DELIVERY_REQ_NUM = 1
;

update tjfax157_cr_deliv
set
    CUST_DEM_CR_IN_DATE = '20240322',
    CUST_DEM_CR_OUT_DATE = '20240322'
--    CUST_DEM_CR_IN_TIME_ZONE_CTGR = null
where
        cr_num = 'Åyíuä∑ï∂éöóÒ3Åz'
    AND
        DELIVERY_REQ_NUM = 2
;

update tjfax157_cr_deliv
set
    CUST_DEM_CR_IN_DATE = '20240322',
    CUST_DEM_CR_OUT_DATE = '20240322'
--    CUST_DEM_CR_IN_TIME_ZONE_CTGR = null
where
        cr_num = 'Åyíuä∑ï∂éöóÒ3Åz'
    AND
        DELIVERY_REQ_NUM = 3
;
--éÛíçî¿ì¸èoñæç◊
select cr_num,DELIVERY_REQ_NUM,CUST_DEM_CR_IN_DATE,CUST_DEM_CR_OUT_DATE from tjfax157_cr_deliv a
where cr_num = 'Åyíuä∑ï∂éöóÒ3Åz';

--commit;


