SELECT output FROM TABLE(
    DBMS_WORKLOAD_REPOSITORY.AWR_REPORT_HTML(
        (SELECT dbid FROM v$database),
        (SELECT instance_number FROM v$instance),
        (SELECT max(snap_id) - 1 FROM dba_hist_snapshot),
        (SELECT max(snap_id) FROM dba_hist_snapshot)
    )
)