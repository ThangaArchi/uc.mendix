create or replace function {{FUNCTION-NAME_FROM-RANGE-ID}}  (I_SET_ID int)
returns int
as
$body$
declare
ERRORCODE	INT := 0;
begin
/* 
Set name {{FUNCTION-NAME_FROM-RANGE-ID}}

*/ 
  insert into SET_Contents (SetId, ObjectId)
   select distinct I_SET_ID, o.OBJECT_ID
  from CTT_OBJECT_APPLICATIONS o where o.OBJECT_TYPE in 
  		(select IdTyp from TypCat where IdCatParent in                   
  				(select IdCat from Cat where CatNam = '{{RULE_CATEGORY_NAME}}'));
  
return ERRORCODE;
end;
$body$
LANGUAGE plpgsql
/




