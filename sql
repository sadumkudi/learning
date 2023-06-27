SELECT a.alarminc_no
FROM event_history AS a WITH (NOLOCK)
LEFT JOIN event_history AS b WITH (NOLOCK)
    ON a.alarminc_no = b.alarminc_no
    AND b.event_id = 'AA'
WHERE a.alarminc_no IS NOT NULL
    AND a.event_date BETWEEN DATEADD(hh, -1, GETDATE()) AND DATEADD(hh, +1, GETDATE())
    AND a.event_id IN ('101', '102')
    AND b.event_date IS NULL;
