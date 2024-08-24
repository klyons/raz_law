from justopinion import CAPClient

client = CAPClient(api_token='49eb70bc06a32b6ec66b336ddcb5d68a6d010214')


#this is our code example for pulling data from the law library
def example():
	oracle_download = client.fetch(query="750 F.3d 1339")
	#oracle_case = client.read_cite("750 F.3d 1339", full_case=True)
	print(oracle_download)