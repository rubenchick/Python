INSERT INTO test_marketing (`Date`, Account_Name, Cost, number_leads)
    SELECT sources.`Date`, sources.Account_Name, sources.Cost, IFNULL(number_leads, 0) as number_leads
    FROM (
        SELECT *
        FROM raw_data.google_ads ga
        WHERE ga.`Date` BETWEEN DATE_FORMAT(now() - interval 30 day,'%Y-%m-%d %00:%00:%00') AND DATE_FORMAT(now(),'%Y-%m-%d %00:%00:%00')
        UNION ALL
        SELECT *
        FROM raw_data.yandex_direct yd
        WHERE yd.`Date` BETWEEN DATE_FORMAT(now() - interval 30 day,'%Y-%m-%d %00:%00:%00') AND DATE_FORMAT(now(),'%Y-%m-%d %00:%00:%00')
    ) as sources
    LEFT JOIN (
        SELECT Date_Create, Account_Name, COUNT(*) as number_leads
        FROM raw_data.crm_deals td
        WHERE td.Date_Create BETWEEN DATE_FORMAT(now() - interval 30 day,'%Y-%m-%d %00:%00:%00') AND DATE_FORMAT(now(),'%Y-%m-%d %00:%00:%00')
        GROUP BY Date_Create, Account_Name
    ) as leads ON sources.`Date` = leads.Date_Create AND sources.Account_Name = leads.Account_Name
ON DUPLICATE KEY UPDATE
    Cost = VALUES(Cost),
    number_leads = VALUES(number_leads)