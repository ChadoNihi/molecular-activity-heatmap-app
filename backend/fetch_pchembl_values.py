from chembl_webresource_client.new_client import new_client

TARGETS = [
	"CHEMBL325",
	"CHEMBL1937",
	"CHEMBL1829",
	"CHEMBL3524",
	"CHEMBL2563",
	"CHEMBL1865",
	"CHEMBL2716",
	"CHEMBL3192",
	"CHEMBL4145",
	"CHEMBL5103",
	"CHEMBL3310"]
MOLECULES = [
	"CHEMBL98",
	"CHEMBL99",
	"CHEMBL27759",
	"CHEMBL2018302",
	"CHEMBL483254",
	"CHEMBL1213490",
	"CHEMBL356769",
	"CHEMBL272980",
	"CHEMBL430060",
	"CHEMBL1173445",
	"CHEMBL356066",
	"CHEMBL1914702"]

def fetch_pchembl_values(target, molecule, activity_client):
	activities = activity_client.filter(
		molecule_chembl_id="CHEMBL98",
		target_chembl_id="CHEMBL1937",
		pchembl_value__isnull=False)

	return list(activity["pchembl_value"]
		for activity in activities if "pchembl_value" in activity)

def save_data_to_json(data, file_name):
	json_ext = ".json"
	# FIXME: make sure data/ dir is create in backend/ dir
	file_path = "./data/" + (
		file_name if file_name.endswith(json_ext) else file_name + json_ext)
	import os
	os.makedirs(os.path.dirname(file_path), exist_ok=True)
	with open(file_path, "w", encoding="utf-8") as f:
		import json
		json.dump(data, f, ensure_ascii=False)


activity_client = new_client.activity
pchembl_values = { target: { molecule:
	fetch_pchembl_values(target, molecule, activity_client)
		for molecule in MOLECULES } for target in TARGETS }

save_data_to_json(pchembl_values, "pchembl_values")
