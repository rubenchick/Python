MERGE INTO test_marketing AS target
USING (
		SELECT  sources.*
			, IFNULL(number_leads,0) as number_leads
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
					SELECT Date_Create, Account_Name
						, COUNT(*) as number_leads
					FROM raw_data.crm_deals cd
					WHERE cd.Date_Create BETWEEN DATE_FORMAT(now() - interval 30 day,'%Y-%m-%d %00:%00:%00') AND DATE_FORMAT(now(),'%Y-%m-%d %00:%00:%00')
					GROUP BY Date_Create, Account_Name
				) as leads ON sources.`Date` = leads.Date_Create AND sources.Account_Name = leads.Account_Name
) AS source  ON target.`Date` = source.`Date` AND target.Account_Name = source.Account_Name
WHEN MATCHED THEN
    UPDATE SET target.Cost = source.Cost
    	, target.number_leads = source.number_leads
WHEN NOT MATCHED BY TARGET THEN
    INSERT (Cost, number_leads) VALUES (source.Cost, source.number_leads)









r_leads)