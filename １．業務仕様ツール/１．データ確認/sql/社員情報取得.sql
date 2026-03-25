select B.emp_cd ||','||
b.EMP_NAME        ||','||
b.EMPLOYEE_NUM        ||','||
A.ORG_NAME          ||','||
b.SG_USER_ID
 from TJFXX04E_ORG_BASIC_M a,TJFXX049_EMP_BASIC_M b
where a.sect_cd=b.sect_cd and emp_cd in ('&1');

exit;

