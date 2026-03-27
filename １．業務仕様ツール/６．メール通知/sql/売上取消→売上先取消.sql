select a.inquiry_num,a.SALES_TO_CANCEL_DATETIME from TJFAX151_CUSTOMER_REQUEST a,TJFAX15A_CR_ITEM b
where a.SALES_TO_CANCEL_DATETIME > '2026/03/27 14:00:00'
 and a.cr_num=b.cr_num
 and b.SALES_STATUS='20'
 and a.inquiry_num like 'JS%'
