--@%OneDrive%\ツール\コマンド実行\Ｚ．共通\共通設定.sql

--実行したSQL文を表示しない
SET ECHO OFF 
SET PAGES 0
SET LINESIZE  2000 COLSEP,
SET SERVEROUTPUT ON
--SET TAB ON
--SET TRIMSPOOL ON
-- 実行時の接続情報やバージョン情報の表示を無効化
--SET TERMOUT OFF
--変数表示しない
SET VERIFY OFF
--alter session set nls_date_format='YYYY/MM/DD HH24:MI:SS';
set heading On


--サンプル　HE100152841　30885
select '問合せ番号,問合せ明細番号,受注商品コード,受注数量,実在庫引当済数量,最終入庫予定年月日,最終入庫予定引当数量,物流進捗ステータス' from dual;
select
INQUIRY_NUM ||','||
INQUIRY_L_NUM ||','||
CR_ITEM_CD ||','||
CR_QTY ||','||
REAL_INV_ALLOC_QTY  ||','||
LAST_STKIN_PLAN_DATE ||','||
LAST_STKIN_PLAN_ALLOC_QTY ||','||
CASE DIST_PROGRESS_STATUS
    WHEN '10' THEN 'オーダー連携済'
    WHEN '20' THEN '手配中'
    WHEN '30' THEN '出荷完了'
    WHEN '40' THEN '納品完了'
    WHEN '50' THEN '第一納品先納品完了'
    WHEN '51' THEN '第一納品先手配中'
    WHEN '52' THEN '第一納品先出荷完了'
    WHEN '53' THEN '入荷完了キッティング待ち'
    WHEN '54' THEN 'キッティング完了入荷待ち'
    WHEN '55' THEN '第一納品先出荷準備完了'
    WHEN '56' THEN '第一納品先オーダー連携済'
    WHEN '60' THEN '60:第一納品先への納品完了'
    WHEN '61' THEN '61:第一納品先手配中'
    WHEN '62' THEN '62:第一納品先からの出荷完了'
    WHEN '70' THEN '70:設置完了'
    WHEN '91' THEN '未設定'
  END 
--"問合せ番号,問合せ明細番号,受注商品コード,受注数量,実在庫引当済数量,最終入庫予定年月日,最終入庫予定引当数量,物流進捗ステータス"
from TJFAX15A_CR_ITEM where inquiry_num='&1' and inquiry_l_num='&2' and l_flg='1' and cancel_flg='0';

exit;
