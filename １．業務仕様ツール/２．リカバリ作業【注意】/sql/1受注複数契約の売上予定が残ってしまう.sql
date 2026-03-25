--■消込対象の売上予定特定
SET ECHO ON
SET LINESIZE 1000 PAGES 1000 COLSEP,
SELECT
    sales_planed_num 売上予定番号,
    SUBSTR(disp_inquiry_num_list,1,11) 問合せ番号,
    sales_booking_flg 売上計上済フラグ,
    sales_planed_invalid_flg 売上予定無効フラグ
FROM
    tjfax691_sales_planed
WHERE
    sales_planed_num IN ( '【置換文字列1】', '', '' );

--■売上予定消込(このケースは、売りあがっているので、売上予定無効フラグではなく、売上計上済フラグをON)
UPDATE tjfax691_sales_planed
SET
    sales_booking_flg = '1' --売上計上済フラグ
WHERE
    sales_planed_num IN ( '【置換文字列1】', '', '' )
    AND sales_booking_flg = '0'
    AND sales_planed_invalid_flg = '0';
    
----COMMIT;

