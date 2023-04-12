SELECT DISTINCT	number_phones
	, (COUNT() OVER (PARTITION BY number_phones) * 100 / COUNT() OVER ()) || '%' as percent -- for SQLite
--	, CONCAT(COUNT() OVER (PARTITION BY number_phones)  / COUNT() OVER (), '%') as percent -- for MySQL
FROM (
	-- подсчет кол-ва телефонов у контакта. Тут можно добавить доп фильтры по уникальности номера  и т.д.
	SELECT contact_id
		, COUNT(DISTINCT phone_id) as number_phones
	FROM (
		-- каждый телефон отдельной записью
		SELECT Contact_ID as contact_id
	    	, JSON_EXTRACT(json_each.value, '$.ID') AS phone_id
	    FROM crm_contacts, json_each(crm_contacts.PHONE)
	) raw_data
	GROUP BY contact_id
) main
ORDER BY number_phones