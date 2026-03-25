set echo on
column spool_filename new_value spool_filename

select 'saito' spool_filename from dual;
spool &spool_filename

select sysdate from dual;

exit;
