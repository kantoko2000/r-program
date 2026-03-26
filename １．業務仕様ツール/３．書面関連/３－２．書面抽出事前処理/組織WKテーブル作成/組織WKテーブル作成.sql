@C:\íËå^çÏã∆\ã§í \ã§í ê›íË.sql
-----------------------------------------------------------------------------------------------

SHOW USER;

DELETE WK_SOSIKI_1;
COMMIT;
INSERT INTO WK_SOSIKI_1
SELECT
vjmox011.orb_org_id,
    vjmox011.orb_cubic_org_id
FROM
    (
        SELECT
            t.orb_org_id,
            t.orb_cubic_org_id
        FROM
            vjmox011_mv_org_basic t
        WHERE
            t.orb_start_date <= SYSDATE
            AND t.orb_start_date = (
                SELECT
                    MAX(orb_start_date)
                FROM
                    vjmox011_mv_org_basic t2
                WHERE
                    t2.orb_org_id = t.orb_org_id
            )
    ) vjmox011
;
COMMIT;

DELETE WK_SOSIKI_2;
COMMIT;

INSERT INTO WK_SOSIKI_2
SELECT
c.corp_id,
a.orb_org_id,
    b.department_name
FROM
    vjmox011_mv_org_basic        a,
    vjmox014_mv_org_cubic_dept   b,
    vjmox009_mv_company          c
WHERE 1=1
--    a.orb_org_id = level1_org_id
    AND a.orb_end_date >= SYSDATE
    AND a.orb_cubic_org_id = b.cubic_org_id
    AND b.cubic_corp_id = c.cubic_corp_id
    AND b.end_date >= SYSDATE
--    AND c.corp_id = company_cd
    AND c.end_date >= SYSDATE
;
COMMIT;


exit;
