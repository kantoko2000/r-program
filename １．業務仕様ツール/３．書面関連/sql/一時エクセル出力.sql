select substr(CREATE_DATETIME,1,7),count(*) from TJFAX01J_DOC_INSPECT_CNT_LINE group by substr(CREATE_DATETIME,1,7) order by 1 desc
