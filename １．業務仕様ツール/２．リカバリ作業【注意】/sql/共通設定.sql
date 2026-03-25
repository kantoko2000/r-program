SET ECHO OFF 
SET PAGES 200
SET LINESIZE  2000 COLSEP,
SET SERVEROUTPUT ON
SET TAB ON
SET TRIMSPOOL ON
SET TERMOUT OFF
alter session set nls_date_format='YYYY/MM/DD HH24:MI:SS';
set heading OFF
SET VERIFY ON    
--ê⁄ë±ÉÜÅ[ÉUéÊìæ
select sys_context('USERENV','SESSION_USER') || '@' || sys_context('USERENV','INSTANCE_NAME') "UESR_NAME" from dual;
column connuser new_value connuser
select sys_context('USERENV','SESSION_USER') || '_'  ||sys_context('USERENV','INSTANCE_NAME') connuser from dual;
SET ECHO ON
set heading oN
SET TERMOUT oN
