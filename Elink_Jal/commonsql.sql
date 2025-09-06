delete from m_location where location_id > 2;
alter sequence m_location_location_id_seq restart with 3;
select * from m_location;