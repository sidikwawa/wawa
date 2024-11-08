from faker import Faker
from bs4 import BeautifulSoup as bs
import requests, re, time, base64, struct, binascii, random, sys, pytz, os, uuid, json, string
from rich.console import Console
from datetime import datetime
from urllib.parse import urlparse
import random


Ok, Cp, Fail = 0,0,0
console = Console()

L =  '\033[4m'
I = '\033[3m'
P = '\033[0m'
M = '\x1b[1;91m'
H = "\033[32m"
K = '\x1b[1;93m'
G = "\033[35m"
A = "\033[1;30m"
space = ""


# # Memilih fb_device secara acak
fb_device = random.choice(["MZB8IN", "M3KG", "M13KH", "M13KH", "21091116UI", "2201123G", "2201123C", "2203129G", "2201122C", "2201122G", "2203121C", "22071212AG", "22081212UG", "2112123AC", "2112123AG", "23127PN0CC", "SKR-H0", "SKR-A0", "SKW-H0", "SKW-A0", "DLT-A0", "DLT-H0", "KLE-H0", "KLE-A0", "SHARK MBU-A0", "SHARK MBU-H0", "SHARK PRS-H0", "SHARK PRS-A0", "SHARK KSR-A0", "SHARK KTUS-H0", "2109119BC", "2209129SC", "M2002J9G", "M2002J9S", "M2102J2SC", "M2007J3SY", "M2007J3SG", "M2007J3SP", "M2007J3SI", "M2007J17C", "M2011K2C", "M2102K1AC", "M2102K1G", "M2012K11G", "M2012K11AI", "M2012K11I", "2015015", "2016070", "M1808D2TG", "M1904F3BG", "M1903F2G", "M1903F11G", "M1906F9SH", "M1803D5XA", "M1810E5GG", "M2011J18C", "M1910F4G", "M2002F4LG", "M1910F4G", "M1910F4S", "M1901F9E", "M1805E10A", "21061119AG", "21061119DG", "21061119AL", "22011119TI", "22071219AI"])
headers = {
    "host": "b-graph.facebook.com",
    "x-fb-ta-logging-ids": "graphql:b2a80809-bfe5-43bb-971b-ead42a5e57ed",
    "authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
    "content-type": "application/x-www-form-urlencoded",
    "x-graphql-request-purpose": "fetch",
    "x-fb-sim-hni": str(random.randint(10000, 99999)),
    "x-fb-background-state": "1",
    "x-fb-net-hni": str(random.randint(10000, 99999)),
    "x-fb-request-analytics-tags": '{"network_tags":{"product":"350685531728","purpose":"fetch","request_category":"graphql","retry_attempt":"0"},"application_tags":"graphservice"}',
    "x-graphql-client-library": "graphservice",
    "x-fb-friendly-name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.reg.name.async",
    "x-fb-privacy-context": "3643298472347298",
    # "user-agent": user_agent,
    "user-agent": f"[FBAN/FB4A;FBAV/485.0.0.70.77;FBBV/543547945;FBDM/density=2.75,width=1080,height=2167;FBLC/id_ID;FBRV/0;FBCR/Telkomsel;FBMF/Xiaomi;FBBD/POCO;FBPN/com.facebook.katana;FBDV/{fb_device};FBSV/12;FBOP/1;FBCA/arm64-v8a:;]",
    "x-fb-connection-type": "MOBILE.LTE",
    "x-fb-device-group": str(random.randint(1000, 9999)),
    "x-tigon-is-retry": "False",
    "priority": "u=3,i",
    "x-fb-http-engine": "Liger",
    "x-fb-client-ip": "True",
    "x-fb-server-cluster": "True"
}


class MainProcess:
	def __init__(self):
		self.settings()
	
	def display_author(self):
		nan = ''
	
	def settings(self):
		self.display_author()
		global total, delay, umail, pwx, nama, cln, thn
		umail = "random"
		pwx = "random"
		cln = "random"
		thn = "random"
		AccountCreation()
		self.run_loop()
	
	def run_loop(self):
		os.system("python3 nonproxy1.py")

class AccountCreation:
	def __init__(self):
		self.ses = requests.Session()
		self.mail= requests.Session()
		self.ses.cookies.clear()
		self.mail.cookies.clear()
		self.headers = headers
		self.head_mail =  {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Sec-Ch-Ua':'','Sec-Ch-Ua-Mobile':'?1','Sec-Ch-Ua-Platform':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'none','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Linux; Android 11; vivo 1918 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.0000.00 Mobile Safari/537.36'}
		self.data_collection()
		self.name_signup()
	
	def data_collection(self):
		self.first_name, self.last_name = self.generate_username()
		if umail == "random":
			self.email, self.ses_email, self.tim_email, self.cookie_email = self.get_email_tempio() #self.get_email_10minutemail()
		else:
			self.email, self.ses_email, self.tim_email, self.cookie_email = self.get_email_tempio() #self.get_email_10minutemail()
		self.birth_date = self.generate_birthday()
		self.password = self.generate_password()
	
	def generate_username(self):
		if cln == "random":
			nm = random.choice(['id_ID'])
			fake = Faker(nm)
			first_name = fake.first_name_female()
			last_name = fake.last_name_female()
			name = f"{first_name} {last_name}"
			return first_name, last_name
		return "user" + ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(5))
	
	def generate_birthday(self):
		if thn == "random":
			year = random.randint(1980, 2003)
			month = random.randint(1, 12)
			day = random.randint(1, 28)
			birth = f'{day:02d}-{month:02d}-{year}'
			return birth
		return "1-2-1999"
	
	def generate_password(self):
		if pwx == "random":
			return "Bandung12@"
		return "Bandung12@"
	
	def get_crypto(self):
		ses = requests.Session()
		nam = ''.join(random.choices(string.ascii_lowercase, k=8))
		jam = str(datetime.now().strftime("%X")).replace(':', '') 
		ran = str(random.randrange(1000, 10000))
		email = f"{nam}.{jam}.{ran}@labworld.org"
		while True:
				try:
					raun = ses.get("https://cryptogmail.com/api/emails?inbox=" + email).text		
					if "404" in raun:
						return email, None, None, None  # Return valid tuple even if no email found	
					elif "data" in raun:
						z = json.loads(raun)
						for data in z["data"]:
							got = json.loads(ses.get("https://cryptogmail.com/api/emails/" + data["id"]).text)
							ses_email = got.get("email")  # Extract the email from the 'got' response as an example
							tim_email = got.get("time")	# Example for time
							cookie_email = got.get("cookie") # Example for cookie
							# Process the email data here (add your logic)
							break  # Exit after processing the first email data	
					return email, ses_email, tim_email, cookie_email  # Ensure all variables are returned
				
				except ConnectionError:
					print("Jaringan terputus! Mencoba kembali dalam 5 detik...")
					time.sleep(40)  # Tunggu 30 detik sebelum mencoba lagi

	def get_code_crypto(self):
		ses = requests.Session()
		email = self.email
		while True:  # Loop untuk mencoba kembali jika terjadi error
			try:
				response = ses.get(f"https://cryptogmail.com/api/emails?inbox={email}")

				# If the request fails or doesn't return a successful status
				if response.status_code != 200:
					print(f"Failed to fetch emails for {email}. Status code: {response.status_code}")
					return None

				raun = response.text

				if "404" in raun:
					return None  # No emails found
				elif "data" in raun:
					z = json.loads(raun)
					for data in z.get("data", []):  # Safely get the 'data' key
						email_data = ses.get(f"https://cryptogmail.com/api/emails/{data['id']}").text
						got = json.loads(email_data)
						subject = got.get("data", {}).get("subject", "")  # Safely get the subject
						# Use regex to extract the 5-digit confirmation code
						kode_match = re.search(r'\b(\d{5})\b', subject)
						if kode_match:
							return kode_match.group(1)  # Return the confirmation cod
				# If no valid code was found
				print(f"Email: {self.email} verification failed")
				with open('data/RegistrasiCodeGagal.txt', 'a') as file:
					file.write(f"{self.email}\n")

			except ConnectionError:
				print("Jaringan terputus! Mencoba kembali dalam 5 detik...")
				time.sleep(40)  # Tunggu 5 detik sebelum mencoba lagi

			except Exception as e:
				print(f"Error occurred: {str(e)}")
				return None

	def get_email_11sec(self): 
		nam = ''.join(random.choices(string.ascii_lowercase, k=8))
		jam = str(datetime.now().strftime("%X")).replace(':', '') 
		ran = str(random.randrange(1000, 10000))
		#dom = random.choice(['1secmail.com', '1secmail.org', '1secmail.net','dpptd.com'])
		dom = random.choice(['1secmail.org'])
		email = f'{nam}.{jam}.{ran}@{dom}'
		cookie_email = ''
		ses_email = ''
		tim_email = ''
		cookie_email = ''
		return email, ses_email, tim_email, cookie_email

	def get_code_1sec(self):
		name, domain = self.email.split('@')
		req = self.ses.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={name}&domain={domain}').json()
		if req:
			subject = req[0].get('subject', '')
			code = re.search(r'\d+', subject)		
			if code:
				return code.group()  
			else:
				return "Kode tidak ditemukan"
		else:
			return "Tidak ada pesan"
	
	def get_email_10minutemail(self):
		req = bs(self.mail.get('https://10minutemail.net/m/?lang=id', headers=self.head_mail, allow_redirects=True).content, 'html.parser')
		ses_email = re.search('sessionid="(.*?)"', str(req)).group(1)
		tim_email = str(time.time()).replace('.', '')[:13]
		dat = {'new': '1', 'sessionid': ses_email, '_': tim_email}
		pos = self.mail.post('https://10minutemail.net/address.api.php', data=dat, headers=self.head_mail, allow_redirects=True).json()
		email = pos['mail_get_mail']
		cookie_email = '; '.join([f"{x}={y}" for x, y in self.mail.cookies.get_dict().items()])
		return email, ses_email, tim_email, cookie_email
	
	def get_code_10minutemail(self):
		dat = {'new':'0','sessionid':self.ses_email,'_':self.tim_email}
		pos = self.mail.post('https://10minutemail.net/address.api.php',data=dat,headers=self.head_mail,cookies={'cookie':self.cookie_email},allow_redirects=True).json()
		subject = pos.get('mail_list', [])[0].get('subject', '')
		kode = re.search(r'(\d{5})', subject).group(1)
		return(kode)

	def get_email_tempio(self,minLen=10, maxLen=10):
		session = requests.session()
		session.headers.update({"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3","accept-encoding": "gzip, deflate, br","accept-language": "en-US,en;q=0.9","upgrade-insecure-requests": "1","user-agent": "Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0"})
		session.get("https://temp-mail.io/en")
		data = {
        "min_name_length": str(minLen),
        "max_name_length": str(maxLen)}
		response = session.post("https://api.internal.temp-mail.io/api/v2/email/new", data=data)
		email = json.loads(response.text)["email"]
		ses_mail = ""
		ses_email = ''
		tim_email = ''
		cookie_email = ''
		return email, ses_email, tim_email, cookie_email
	
	def get_code_tempio(self):
		session = requests.session()
		email = self.email
		response = session.get(f"https://api.internal.temp-mail.io/api/v2/email/{email}/messages")
		messages = response.content.decode("utf-8")
		match = re.search(r'\b\d{5}\b', messages)
		if match:
			code = match.group(0)
			return code
		else:
			return None

	def name_signup(self):
		global Fail
		print(f"\rnama: {self.first_name} {self.last_name}     ", end = '')
		try:
			# Proxy URL dengan autentikasi
			proxy_url = 'http://7clptii6e4udqdc-session-1pkfwqpz3h-lifetime-2:bp5qcvv0l3iuje8@rp.proxyscrape.com:6060'
			parsed_proxy = urlparse(proxy_url)
			prox = {
				'http': f"{parsed_proxy.scheme}://{parsed_proxy.netloc}",
				'https': f"{parsed_proxy.scheme}://{parsed_proxy.netloc}"
			}
			data = {
				'method': 'post',
				'pretty': False,
				'format': 'json',
				'server_timestamps': True,
				'locale': 'id_ID',
				'purpose': 'fetch',
				'fb_api_req_friendly_name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.reg.name.async',
				'fb_api_caller_class': 'graphservice',
				'client_doc_id': '11994080423068421059028841356',
				'variables': json.dumps({"params":{"params":"{\"params\":\"{\\\"client_input_params\\\":{\\\"lois_settings\\\":{\\\"lois_token\\\":\\\"\\\",\\\"lara_override\\\":\\\"\\\"},\\\"firstname\\\":\\\""+self.first_name+"\\\",\\\"lastname\\\":\\\""+self.last_name+"\\\"},\\\"server_params\\\":{\\\"event_request_id\\\":\\\""+str(uuid.uuid4())+"\\\",\\\"is_from_logged_out\\\":0,\\\"layered_homepage_experiment_group\\\":null,\\\"device_id\\\":\\\"00776e25-3a07-474d-b1f6-2063f29fa49f\\\",\\\"waterfall_id\\\":\\\"24f9d94d-8ed0-4a0b-9e0c-7f11379c67b3\\\",\\\"INTERNAL__latency_qpl_instance_id\\\":4.0265740600288E13,\\\"flow_info\\\":\\\"{\\\\\\\"flow_name\\\\\\\":\\\\\\\"new_to_family_fb_default\\\\\\\",\\\\\\\"flow_type\\\\\\\":\\\\\\\"ntf\\\\\\\"}\\\",\\\"is_platform_login\\\":0,\\\"INTERNAL__latency_qpl_marker_id\\\":36707139,\\\"reg_info\\\":\\\"{\\\\\\\"first_name\\\\\\\":null,\\\\\\\"last_name\\\\\\\":null,\\\\\\\"full_name\\\\\\\":null,\\\\\\\"contactpoint\\\\\\\":null,\\\\\\\"ar_contactpoint\\\\\\\":null,\\\\\\\"contactpoint_type\\\\\\\":null,\\\\\\\"is_using_unified_cp\\\\\\\":null,\\\\\\\"unified_cp_screen_variant\\\\\\\":null,\\\\\\\"is_cp_auto_confirmed\\\\\\\":false,\\\\\\\"is_cp_auto_confirmable\\\\\\\":false,\\\\\\\"confirmation_code\\\\\\\":null,\\\\\\\"birthday\\\\\\\":null,\\\\\\\"did_use_age\\\\\\\":null,\\\\\\\"gender\\\\\\\":null,\\\\\\\"use_custom_gender\\\\\\\":false,\\\\\\\"custom_gender\\\\\\\":null,\\\\\\\"encrypted_password\\\\\\\":null,\\\\\\\"username\\\\\\\":null,\\\\\\\"username_prefill\\\\\\\":null,\\\\\\\"fb_conf_source\\\\\\\":null,\\\\\\\"device_id\\\\\\\":\\\\\\\"00776e25-3a07-474d-b1f6-2063f29fa49f\\\\\\\",\\\\\\\"ig4a_qe_device_id\\\\\\\":null,\\\\\\\"family_device_id\\\\\\\":\\\\\\\"00776e25-3a07-474d-b1f6-2063f29fa49f\\\\\\\",\\\\\\\"nta_eligibility_reason\\\\\\\":null,\\\\\\\"ig_nta_test_group\\\\\\\":null,\\\\\\\"user_id\\\\\\\":null,\\\\\\\"safetynet_token\\\\\\\":null,\\\\\\\"safetynet_response\\\\\\\":null,\\\\\\\"machine_id\\\\\\\":null,\\\\\\\"profile_photo\\\\\\\":null,\\\\\\\"profile_photo_id\\\\\\\":null,\\\\\\\"profile_photo_upload_id\\\\\\\":null,\\\\\\\"avatar\\\\\\\":null,\\\\\\\"email_oauth_token_no_contact_perm\\\\\\\":null,\\\\\\\"email_oauth_token\\\\\\\":null,\\\\\\\"email_oauth_tokens\\\\\\\":null,\\\\\\\"should_skip_two_step_conf\\\\\\\":null,\\\\\\\"openid_tokens_for_testing\\\\\\\":null,\\\\\\\"encrypted_msisdn\\\\\\\":null,\\\\\\\"encrypted_msisdn_for_safetynet\\\\\\\":null,\\\\\\\"cached_headers_safetynet_info\\\\\\\":null,\\\\\\\"should_skip_headers_safetynet\\\\\\\":null,\\\\\\\"headers_last_infra_flow_id\\\\\\\":null,\\\\\\\"headers_last_infra_flow_id_safetynet\\\\\\\":null,\\\\\\\"headers_flow_id\\\\\\\":null,\\\\\\\"was_headers_prefill_available\\\\\\\":null,\\\\\\\"sso_enabled\\\\\\\":null,\\\\\\\"existing_accounts\\\\\\\":null,\\\\\\\"used_ig_birthday\\\\\\\":null,\\\\\\\"sync_info\\\\\\\":null,\\\\\\\"create_new_to_app_account\\\\\\\":null,\\\\\\\"skip_session_info\\\\\\\":null,\\\\\\\"ck_error\\\\\\\":null,\\\\\\\"ck_id\\\\\\\":null,\\\\\\\"ck_nonce\\\\\\\":null,\\\\\\\"should_save_password\\\\\\\":null,\\\\\\\"horizon_synced_username\\\\\\\":null,\\\\\\\"fb_access_token\\\\\\\":null,\\\\\\\"horizon_synced_profile_pic\\\\\\\":null,\\\\\\\"is_identity_synced\\\\\\\":false,\\\\\\\"is_msplit_reg\\\\\\\":null,\\\\\\\"user_id_of_msplit_creator\\\\\\\":null,\\\\\\\"dma_data_combination_consent_given\\\\\\\":null,\\\\\\\"xapp_accounts\\\\\\\":null,\\\\\\\"fb_device_id\\\\\\\":null,\\\\\\\"fb_machine_id\\\\\\\":null,\\\\\\\"ig_device_id\\\\\\\":null,\\\\\\\"ig_machine_id\\\\\\\":null,\\\\\\\"should_skip_nta_upsell\\\\\\\":null,\\\\\\\"big_blue_token\\\\\\\":null,\\\\\\\"skip_sync_step_nta\\\\\\\":null,\\\\\\\"caa_reg_flow_source\\\\\\\":\\\\\\\"login_home_native_integration_point\\\\\\\",\\\\\\\"ig_authorization_token\\\\\\\":null,\\\\\\\"full_sheet_flow\\\\\\\":false,\\\\\\\"crypted_user_id\\\\\\\":null,\\\\\\\"is_caa_perf_enabled\\\\\\\":true,\\\\\\\"is_preform\\\\\\\":true,\\\\\\\"ignore_suma_check\\\\\\\":false,\\\\\\\"ignore_existing_login\\\\\\\":false,\\\\\\\"ignore_existing_login_from_suma\\\\\\\":false,\\\\\\\"ignore_existing_login_after_errors\\\\\\\":false,\\\\\\\"suggested_first_name\\\\\\\":null,\\\\\\\"suggested_last_name\\\\\\\":null,\\\\\\\"suggested_full_name\\\\\\\":null,\\\\\\\"replace_id_sync_variant\\\\\\\":null,\\\\\\\"is_redirect_from_nta_replace_id_sync_variant\\\\\\\":false,\\\\\\\"frl_authorization_token\\\\\\\":null,\\\\\\\"post_form_errors\\\\\\\":null,\\\\\\\"skip_step_without_errors\\\\\\\":false,\\\\\\\"existing_account_exact_match_checked\\\\\\\":false,\\\\\\\"existing_account_fuzzy_match_checked\\\\\\\":false,\\\\\\\"confirmation_code_send_error\\\\\\\":null,\\\\\\\"is_too_young\\\\\\\":false,\\\\\\\"source_account_type\\\\\\\":null,\\\\\\\"whatsapp_installed_on_client\\\\\\\":false,\\\\\\\"confirmation_medium\\\\\\\":null,\\\\\\\"source_credentials_type\\\\\\\":null,\\\\\\\"source_cuid\\\\\\\":null,\\\\\\\"source_account_reg_info\\\\\\\":null,\\\\\\\"soap_creation_source\\\\\\\":null,\\\\\\\"source_account_type_to_reg_info\\\\\\\":null,\\\\\\\"registration_flow_id\\\\\\\":\\\\\\\"b6199014-914d-4e11-8729-d4078bf7233d\\\\\\\",\\\\\\\"should_skip_youth_tos\\\\\\\":false,\\\\\\\"is_youth_regulation_flow_complete\\\\\\\":false,\\\\\\\"is_on_cold_start\\\\\\\":false,\\\\\\\"email_prefilled\\\\\\\":false,\\\\\\\"cp_confirmed_by_auto_conf\\\\\\\":false,\\\\\\\"auto_conf_info\\\\\\\":null,\\\\\\\"in_sowa_experiment\\\\\\\":false,\\\\\\\"youth_regulation_config\\\\\\\":null,\\\\\\\"conf_allow_back_nav_after_change_cp\\\\\\\":null,\\\\\\\"conf_bouncing_cliff_screen_type\\\\\\\":null,\\\\\\\"conf_show_bouncing_cliff\\\\\\\":null,\\\\\\\"eligible_to_flash_call_in_ig4a\\\\\\\":false,\\\\\\\"flash_call_permissions_status\\\\\\\":null,\\\\\\\"attestation_result\\\\\\\":null,\\\\\\\"request_data_and_challenge_nonce_string\\\\\\\":null,\\\\\\\"confirmed_cp_and_code\\\\\\\":null,\\\\\\\"notification_callback_id\\\\\\\":null,\\\\\\\"reg_suma_state\\\\\\\":0,\\\\\\\"is_msplit_neutral_choice\\\\\\\":false,\\\\\\\"msg_previous_cp\\\\\\\":null,\\\\\\\"ntp_import_source_info\\\\\\\":null,\\\\\\\"youth_consent_decision_time\\\\\\\":null,\\\\\\\"username_screen_experience\\\\\\\":\\\\\\\"control\\\\\\\",\\\\\\\"reduced_tos_test_group\\\\\\\":\\\\\\\"control\\\\\\\",\\\\\\\"should_show_spi_before_conf\\\\\\\":true,\\\\\\\"google_oauth_account\\\\\\\":null,\\\\\\\"is_reg_request_from_ig_suma\\\\\\\":false,\\\\\\\"is_igios_spc_reg\\\\\\\":false,\\\\\\\"device_emails\\\\\\\":null,\\\\\\\"is_toa_reg\\\\\\\":false,\\\\\\\"is_threads_public\\\\\\\":false,\\\\\\\"spc_import_flow\\\\\\\":false,\\\\\\\"caa_play_integrity_attestation_result\\\\\\\":null,\\\\\\\"flash_call_provider\\\\\\\":null,\\\\\\\"name_prefill_variant\\\\\\\":\\\\\\\"move_cp_perms_up_without_dialog\\\\\\\",\\\\\\\"spc_birthday_input\\\\\\\":false}\\\",\\\"family_device_id\\\":\\\"00776e25-3a07-474d-b1f6-2063f29fa49f\\\",\\\"offline_experiment_group\\\":\\\"caa_iteration_v6_perf_fb_2\\\",\\\"INTERNAL_INFRA_THEME\\\":\\\"harm_f,default,default,harm_f\\\",\\\"access_flow_version\\\":\\\"F2_FLOW\\\",\\\"is_from_logged_in_switcher\\\":0,\\\"current_step\\\":1}}\"}","bloks_versioning_id":"c3cc18230235472b54176a5922f9b91d291342c3a276e2644dbdb9760b96deec","app_id":"com.bloks.www.bloks.caa.reg.name.async"},"scale":"3","nt_context":{"using_white_navbar":True,"pixel_ratio":3,"is_push_on":True,"styles_id":"e6c6f61b7a86cdf3fa2eaaffa982fbd1","bloks_version":"c3cc18230235472b54176a5922f9b91d291342c3a276e2644dbdb9760b96deec"}}),
				'fb_api_analytics_tags': '["GraphServices"]',
				'client_trace_id': str(uuid.uuid4())
			}
			post = self.ses.post('https://b-graph.facebook.com/graphql', data=data,  headers=self.headers)
			if "Kapan tanggal lahir Anda?" in post.text:
				self.birthday()
			else:
				Fail+=1
		except Exception as e:print(e)
	
	def birthday(self):
		global Fail
		print(f"\rtanggal lahir: {self.birth_date}           ", end = '')
			# Proxy URL dengan autentikasi
		proxy_url = 'http://7clptii6e4udqdc-session-1pkfwqpz3h-lifetime-2:bp5qcvv0l3iuje8@rp.proxyscrape.com:6060'
		parsed_proxy = urlparse(proxy_url)
		prox = {
			'http': f"{parsed_proxy.scheme}://{parsed_proxy.netloc}",
			'https': f"{parsed_proxy.scheme}://{parsed_proxy.netloc}"
		}
		data = {
			'method': 'post',
			'pretty': False,
			'format': 'json',
			'server_timestamps': True,
			'locale': 'id_ID',
			'purpose': 'fetch',
			'fb_api_req_friendly_name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.reg.birthday.async',
			'fb_api_caller_class': 'graphservice',
			'client_doc_id': '11994080423068421059028841356',
			'variables': json.dumps({"params":{"params":"{\"params\":\"{\\\"client_input_params\\\":{\\\"should_skip_youth_tos\\\":0,\\\"is_youth_regulation_flow_complete\\\":0,\\\"birthday_or_current_date_string\\\":\\\""+self.birth_date+"\\\",\\\"birthday_timestamp\\\":"+str(int(time.time()))+",\\\"lois_settings\\\":{\\\"lois_token\\\":\\\"\\\",\\\"lara_override\\\":\\\"\\\"}},\\\"server_params\\\":{\\\"is_from_logged_out\\\":0,\\\"layered_homepage_experiment_group\\\":null,\\\"device_id\\\":\\\""+str(uuid.uuid4())+"\\\",\\\"waterfall_id\\\":\\\""+str(uuid.uuid4())+"\\\",\\\"INTERNAL__latency_qpl_instance_id\\\":4.0318405500151E13,\\\"flow_info\\\":\\\"{\\\\\\\"flow_name\\\\\\\":\\\\\\\"new_to_family_fb_default\\\\\\\",\\\\\\\"flow_type\\\\\\\":\\\\\\\"ntf\\\\\\\"}\\\",\\\"is_platform_login\\\":0,\\\"INTERNAL__latency_qpl_marker_id\\\":36707139,\\\"reg_info\\\":\\\"{\\\\\\\"first_name\\\\\\\":\\\\\\\""+self.last_name+"\\\\\\\",\\\\\\\"last_name\\\\\\\":\\\\\\\""+self.last_name+"\\\\\\\",\\\\\\\"full_name\\\\\\\":null,\\\\\\\"contactpoint\\\\\\\":null,\\\\\\\"ar_contactpoint\\\\\\\":null,\\\\\\\"contactpoint_type\\\\\\\":null,\\\\\\\"is_using_unified_cp\\\\\\\":null,\\\\\\\"unified_cp_screen_variant\\\\\\\":null,\\\\\\\"is_cp_auto_confirmed\\\\\\\":false,\\\\\\\"is_cp_auto_confirmable\\\\\\\":false,\\\\\\\"confirmation_code\\\\\\\":null,\\\\\\\"birthday\\\\\\\":null,\\\\\\\"did_use_age\\\\\\\":false,\\\\\\\"gender\\\\\\\":null,\\\\\\\"use_custom_gender\\\\\\\":false,\\\\\\\"custom_gender\\\\\\\":null,\\\\\\\"encrypted_password\\\\\\\":null,\\\\\\\"username\\\\\\\":null,\\\\\\\"username_prefill\\\\\\\":null,\\\\\\\"fb_conf_source\\\\\\\":null,\\\\\\\"device_id\\\\\\\":\\\\\\\"00776e25-3a07-474d-b1f6-2063f29fa49f\\\\\\\",\\\\\\\"ig4a_qe_device_id\\\\\\\":null,\\\\\\\"family_device_id\\\\\\\":\\\\\\\"00776e25-3a07-474d-b1f6-2063f29fa49f\\\\\\\",\\\\\\\"nta_eligibility_reason\\\\\\\":null,\\\\\\\"ig_nta_test_group\\\\\\\":null,\\\\\\\"user_id\\\\\\\":null,\\\\\\\"safetynet_token\\\\\\\":null,\\\\\\\"safetynet_response\\\\\\\":null,\\\\\\\"machine_id\\\\\\\":null,\\\\\\\"profile_photo\\\\\\\":null,\\\\\\\"profile_photo_id\\\\\\\":null,\\\\\\\"profile_photo_upload_id\\\\\\\":null,\\\\\\\"avatar\\\\\\\":null,\\\\\\\"email_oauth_token_no_contact_perm\\\\\\\":null,\\\\\\\"email_oauth_token\\\\\\\":null,\\\\\\\"email_oauth_tokens\\\\\\\":null,\\\\\\\"should_skip_two_step_conf\\\\\\\":null,\\\\\\\"openid_tokens_for_testing\\\\\\\":null,\\\\\\\"encrypted_msisdn\\\\\\\":null,\\\\\\\"encrypted_msisdn_for_safetynet\\\\\\\":null,\\\\\\\"cached_headers_safetynet_info\\\\\\\":null,\\\\\\\"should_skip_headers_safetynet\\\\\\\":null,\\\\\\\"headers_last_infra_flow_id\\\\\\\":null,\\\\\\\"headers_last_infra_flow_id_safetynet\\\\\\\":null,\\\\\\\"headers_flow_id\\\\\\\":null,\\\\\\\"was_headers_prefill_available\\\\\\\":null,\\\\\\\"sso_enabled\\\\\\\":null,\\\\\\\"existing_accounts\\\\\\\":null,\\\\\\\"used_ig_birthday\\\\\\\":null,\\\\\\\"sync_info\\\\\\\":null,\\\\\\\"create_new_to_app_account\\\\\\\":null,\\\\\\\"skip_session_info\\\\\\\":null,\\\\\\\"ck_error\\\\\\\":null,\\\\\\\"ck_id\\\\\\\":null,\\\\\\\"ck_nonce\\\\\\\":null,\\\\\\\"should_save_password\\\\\\\":null,\\\\\\\"horizon_synced_username\\\\\\\":null,\\\\\\\"fb_access_token\\\\\\\":null,\\\\\\\"horizon_synced_profile_pic\\\\\\\":null,\\\\\\\"is_identity_synced\\\\\\\":false,\\\\\\\"is_msplit_reg\\\\\\\":null,\\\\\\\"user_id_of_msplit_creator\\\\\\\":null,\\\\\\\"dma_data_combination_consent_given\\\\\\\":null,\\\\\\\"xapp_accounts\\\\\\\":null,\\\\\\\"fb_device_id\\\\\\\":null,\\\\\\\"fb_machine_id\\\\\\\":null,\\\\\\\"ig_device_id\\\\\\\":null,\\\\\\\"ig_machine_id\\\\\\\":null,\\\\\\\"should_skip_nta_upsell\\\\\\\":null,\\\\\\\"big_blue_token\\\\\\\":null,\\\\\\\"skip_sync_step_nta\\\\\\\":null,\\\\\\\"caa_reg_flow_source\\\\\\\":\\\\\\\"login_home_native_integration_point\\\\\\\",\\\\\\\"ig_authorization_token\\\\\\\":null,\\\\\\\"full_sheet_flow\\\\\\\":false,\\\\\\\"crypted_user_id\\\\\\\":null,\\\\\\\"is_caa_perf_enabled\\\\\\\":true,\\\\\\\"is_preform\\\\\\\":true,\\\\\\\"ignore_suma_check\\\\\\\":false,\\\\\\\"ignore_existing_login\\\\\\\":false,\\\\\\\"ignore_existing_login_from_suma\\\\\\\":false,\\\\\\\"ignore_existing_login_after_errors\\\\\\\":false,\\\\\\\"suggested_first_name\\\\\\\":null,\\\\\\\"suggested_last_name\\\\\\\":null,\\\\\\\"suggested_full_name\\\\\\\":null,\\\\\\\"replace_id_sync_variant\\\\\\\":null,\\\\\\\"is_redirect_from_nta_replace_id_sync_variant\\\\\\\":false,\\\\\\\"frl_authorization_token\\\\\\\":null,\\\\\\\"post_form_errors\\\\\\\":null,\\\\\\\"skip_step_without_errors\\\\\\\":false,\\\\\\\"existing_account_exact_match_checked\\\\\\\":false,\\\\\\\"existing_account_fuzzy_match_checked\\\\\\\":false,\\\\\\\"confirmation_code_send_error\\\\\\\":null,\\\\\\\"is_too_young\\\\\\\":false,\\\\\\\"source_account_type\\\\\\\":null,\\\\\\\"whatsapp_installed_on_client\\\\\\\":false,\\\\\\\"confirmation_medium\\\\\\\":null,\\\\\\\"source_credentials_type\\\\\\\":null,\\\\\\\"source_cuid\\\\\\\":null,\\\\\\\"source_account_reg_info\\\\\\\":null,\\\\\\\"soap_creation_source\\\\\\\":null,\\\\\\\"source_account_type_to_reg_info\\\\\\\":null,\\\\\\\"registration_flow_id\\\\\\\":\\\\\\\"b6199014-914d-4e11-8729-d4078bf7233d\\\\\\\",\\\\\\\"should_skip_youth_tos\\\\\\\":false,\\\\\\\"is_youth_regulation_flow_complete\\\\\\\":false,\\\\\\\"is_on_cold_start\\\\\\\":false,\\\\\\\"email_prefilled\\\\\\\":false,\\\\\\\"cp_confirmed_by_auto_conf\\\\\\\":false,\\\\\\\"auto_conf_info\\\\\\\":null,\\\\\\\"in_sowa_experiment\\\\\\\":false,\\\\\\\"youth_regulation_config\\\\\\\":null,\\\\\\\"conf_allow_back_nav_after_change_cp\\\\\\\":null,\\\\\\\"conf_bouncing_cliff_screen_type\\\\\\\":null,\\\\\\\"conf_show_bouncing_cliff\\\\\\\":null,\\\\\\\"eligible_to_flash_call_in_ig4a\\\\\\\":false,\\\\\\\"flash_call_permissions_status\\\\\\\":null,\\\\\\\"attestation_result\\\\\\\":null,\\\\\\\"request_data_and_challenge_nonce_string\\\\\\\":null,\\\\\\\"confirmed_cp_and_code\\\\\\\":null,\\\\\\\"notification_callback_id\\\\\\\":null,\\\\\\\"reg_suma_state\\\\\\\":0,\\\\\\\"is_msplit_neutral_choice\\\\\\\":false,\\\\\\\"msg_previous_cp\\\\\\\":null,\\\\\\\"ntp_import_source_info\\\\\\\":null,\\\\\\\"youth_consent_decision_time\\\\\\\":null,\\\\\\\"username_screen_experience\\\\\\\":\\\\\\\"control\\\\\\\",\\\\\\\"reduced_tos_test_group\\\\\\\":\\\\\\\"control\\\\\\\",\\\\\\\"should_show_spi_before_conf\\\\\\\":true,\\\\\\\"google_oauth_account\\\\\\\":null,\\\\\\\"is_reg_request_from_ig_suma\\\\\\\":false,\\\\\\\"is_igios_spc_reg\\\\\\\":false,\\\\\\\"device_emails\\\\\\\":null,\\\\\\\"is_toa_reg\\\\\\\":false,\\\\\\\"is_threads_public\\\\\\\":false,\\\\\\\"spc_import_flow\\\\\\\":false,\\\\\\\"caa_play_integrity_attestation_result\\\\\\\":null,\\\\\\\"flash_call_provider\\\\\\\":null,\\\\\\\"name_prefill_variant\\\\\\\":\\\\\\\"move_cp_perms_up_without_dialog\\\\\\\",\\\\\\\"spc_birthday_input\\\\\\\":false}\\\",\\\"family_device_id\\\":\\\"00776e25-3a07-474d-b1f6-2063f29fa49f\\\",\\\"offline_experiment_group\\\":\\\"caa_iteration_v6_perf_fb_2\\\",\\\"INTERNAL_INFRA_THEME\\\":\\\"harm_f,default,default,harm_f\\\",\\\"access_flow_version\\\":\\\"F2_FLOW\\\",\\\"is_from_logged_in_switcher\\\":0,\\\"current_step\\\":2}}\"}","bloks_versioning_id":"c3cc18230235472b54176a5922f9b91d291342c3a276e2644dbdb9760b96deec","app_id":"com.bloks.www.bloks.caa.reg.birthday.async"},"scale":"3","nt_context":{"using_white_navbar":True,"pixel_ratio":3,"is_push_on":True,"styles_id":"e6c6f61b7a86cdf3fa2eaaffa982fbd1","bloks_version":"c3cc18230235472b54176a5922f9b91d291342c3a276e2644dbdb9760b96deec"}}),
			'fb_api_analytics_tags': '["GraphServices"]',
			'client_trace_id': str(uuid.uuid4())
		}
		post = self.ses.post('https://b-graph.facebook.com/graphql', data=data,  headers=self.headers)
		if "Apa jenis kelamin Anda?" in post.text:
			self.gender()
		else:
			Fail+=1
	
	def gender(self):
		global Fail
		print(f"\rkelamin: None                ", end = '')
			# Proxy URL dengan autentikasi
		proxy_url = 'http://7clptii6e4udqdc-session-1pkfwqpz3h-lifetime-2:bp5qcvv0l3iuje8@rp.proxyscrape.com:6060'
		parsed_proxy = urlparse(proxy_url)
		prox = {
			'http': f"{parsed_proxy.scheme}://{parsed_proxy.netloc}",
			'https': f"{parsed_proxy.scheme}://{parsed_proxy.netloc}"
		}
		data = {
			'method': 'post',
			'pretty': False,
			'format': 'json',
			'server_timestamps': True,
			'locale': 'id_ID',
			'purpose': 'fetch',
			'fb_api_req_friendly_name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.reg.gender.async',
			'fb_api_caller_class': 'graphservice',
			'client_doc_id': '11994080423068421059028841356',
			'variables': json.dumps({"params":{"params":"{\"params\":\"{\\\"client_input_params\\\":{\\\"device_phone_numbers\\\":[],\\\"gender\\\":1,\\\"pronoun\\\":0,\\\"lois_settings\\\":{\\\"lois_token\\\":\\\"\\\",\\\"lara_override\\\":\\\"\\\"},\\\"custom_gender\\\":\\\"\\\"},\\\"server_params\\\":{\\\"is_from_logged_out\\\":0,\\\"layered_homepage_experiment_group\\\":null,\\\"device_id\\\":\\\"00776e25-3a07-474d-b1f6-2063f29fa49f\\\",\\\"waterfall_id\\\":\\\"24f9d94d-8ed0-4a0b-9e0c-7f11379c67b3\\\",\\\"INTERNAL__latency_qpl_instance_id\\\":4.0340541600168E13,\\\"flow_info\\\":\\\"{\\\\\\\"flow_name\\\\\\\":\\\\\\\"new_to_family_fb_default\\\\\\\",\\\\\\\"flow_type\\\\\\\":\\\\\\\"ntf\\\\\\\"}\\\",\\\"is_platform_login\\\":0,\\\"INTERNAL__latency_qpl_marker_id\\\":36707139,\\\"reg_info\\\":\\\"{\\\\\\\"first_name\\\\\\\":\\\\\\\""+self.first_name+"\\\\\\\",\\\\\\\"last_name\\\\\\\":\\\\\\\""+self.last_name+"\\\\\\\",\\\\\\\"full_name\\\\\\\":null,\\\\\\\"contactpoint\\\\\\\":null,\\\\\\\"ar_contactpoint\\\\\\\":null,\\\\\\\"contactpoint_type\\\\\\\":null,\\\\\\\"is_using_unified_cp\\\\\\\":null,\\\\\\\"unified_cp_screen_variant\\\\\\\":null,\\\\\\\"is_cp_auto_confirmed\\\\\\\":false,\\\\\\\"is_cp_auto_confirmable\\\\\\\":false,\\\\\\\"confirmation_code\\\\\\\":null,\\\\\\\"birthday\\\\\\\":\\\\\\\""+self.birth_date+"\\\\\\\",\\\\\\\"did_use_age\\\\\\\":false,\\\\\\\"gender\\\\\\\":null,\\\\\\\"use_custom_gender\\\\\\\":false,\\\\\\\"custom_gender\\\\\\\":null,\\\\\\\"encrypted_password\\\\\\\":null,\\\\\\\"username\\\\\\\":null,\\\\\\\"username_prefill\\\\\\\":null,\\\\\\\"fb_conf_source\\\\\\\":null,\\\\\\\"device_id\\\\\\\":\\\\\\\"00776e25-3a07-474d-b1f6-2063f29fa49f\\\\\\\",\\\\\\\"ig4a_qe_device_id\\\\\\\":null,\\\\\\\"family_device_id\\\\\\\":\\\\\\\"00776e25-3a07-474d-b1f6-2063f29fa49f\\\\\\\",\\\\\\\"nta_eligibility_reason\\\\\\\":null,\\\\\\\"ig_nta_test_group\\\\\\\":null,\\\\\\\"user_id\\\\\\\":null,\\\\\\\"safetynet_token\\\\\\\":null,\\\\\\\"safetynet_response\\\\\\\":null,\\\\\\\"machine_id\\\\\\\":null,\\\\\\\"profile_photo\\\\\\\":null,\\\\\\\"profile_photo_id\\\\\\\":null,\\\\\\\"profile_photo_upload_id\\\\\\\":null,\\\\\\\"avatar\\\\\\\":null,\\\\\\\"email_oauth_token_no_contact_perm\\\\\\\":null,\\\\\\\"email_oauth_token\\\\\\\":null,\\\\\\\"email_oauth_tokens\\\\\\\":null,\\\\\\\"should_skip_two_step_conf\\\\\\\":null,\\\\\\\"openid_tokens_for_testing\\\\\\\":null,\\\\\\\"encrypted_msisdn\\\\\\\":null,\\\\\\\"encrypted_msisdn_for_safetynet\\\\\\\":null,\\\\\\\"cached_headers_safetynet_info\\\\\\\":null,\\\\\\\"should_skip_headers_safetynet\\\\\\\":null,\\\\\\\"headers_last_infra_flow_id\\\\\\\":null,\\\\\\\"headers_last_infra_flow_id_safetynet\\\\\\\":null,\\\\\\\"headers_flow_id\\\\\\\":null,\\\\\\\"was_headers_prefill_available\\\\\\\":null,\\\\\\\"sso_enabled\\\\\\\":null,\\\\\\\"existing_accounts\\\\\\\":null,\\\\\\\"used_ig_birthday\\\\\\\":null,\\\\\\\"sync_info\\\\\\\":null,\\\\\\\"create_new_to_app_account\\\\\\\":null,\\\\\\\"skip_session_info\\\\\\\":null,\\\\\\\"ck_error\\\\\\\":null,\\\\\\\"ck_id\\\\\\\":null,\\\\\\\"ck_nonce\\\\\\\":null,\\\\\\\"should_save_password\\\\\\\":null,\\\\\\\"horizon_synced_username\\\\\\\":null,\\\\\\\"fb_access_token\\\\\\\":null,\\\\\\\"horizon_synced_profile_pic\\\\\\\":null,\\\\\\\"is_identity_synced\\\\\\\":false,\\\\\\\"is_msplit_reg\\\\\\\":null,\\\\\\\"user_id_of_msplit_creator\\\\\\\":null,\\\\\\\"dma_data_combination_consent_given\\\\\\\":null,\\\\\\\"xapp_accounts\\\\\\\":null,\\\\\\\"fb_device_id\\\\\\\":null,\\\\\\\"fb_machine_id\\\\\\\":null,\\\\\\\"ig_device_id\\\\\\\":null,\\\\\\\"ig_machine_id\\\\\\\":null,\\\\\\\"should_skip_nta_upsell\\\\\\\":null,\\\\\\\"big_blue_token\\\\\\\":null,\\\\\\\"skip_sync_step_nta\\\\\\\":null,\\\\\\\"caa_reg_flow_source\\\\\\\":\\\\\\\"login_home_native_integration_point\\\\\\\",\\\\\\\"ig_authorization_token\\\\\\\":null,\\\\\\\"full_sheet_flow\\\\\\\":false,\\\\\\\"crypted_user_id\\\\\\\":null,\\\\\\\"is_caa_perf_enabled\\\\\\\":true,\\\\\\\"is_preform\\\\\\\":true,\\\\\\\"ignore_suma_check\\\\\\\":false,\\\\\\\"ignore_existing_login\\\\\\\":false,\\\\\\\"ignore_existing_login_from_suma\\\\\\\":false,\\\\\\\"ignore_existing_login_after_errors\\\\\\\":false,\\\\\\\"suggested_first_name\\\\\\\":null,\\\\\\\"suggested_last_name\\\\\\\":null,\\\\\\\"suggested_full_name\\\\\\\":null,\\\\\\\"replace_id_sync_variant\\\\\\\":null,\\\\\\\"is_redirect_from_nta_replace_id_sync_variant\\\\\\\":false,\\\\\\\"frl_authorization_token\\\\\\\":null,\\\\\\\"post_form_errors\\\\\\\":null,\\\\\\\"skip_step_without_errors\\\\\\\":false,\\\\\\\"existing_account_exact_match_checked\\\\\\\":false,\\\\\\\"existing_account_fuzzy_match_checked\\\\\\\":false,\\\\\\\"confirmation_code_send_error\\\\\\\":null,\\\\\\\"is_too_young\\\\\\\":false,\\\\\\\"source_account_type\\\\\\\":null,\\\\\\\"whatsapp_installed_on_client\\\\\\\":false,\\\\\\\"confirmation_medium\\\\\\\":null,\\\\\\\"source_credentials_type\\\\\\\":null,\\\\\\\"source_cuid\\\\\\\":null,\\\\\\\"source_account_reg_info\\\\\\\":null,\\\\\\\"soap_creation_source\\\\\\\":null,\\\\\\\"source_account_type_to_reg_info\\\\\\\":null,\\\\\\\"registration_flow_id\\\\\\\":\\\\\\\"b6199014-914d-4e11-8729-d4078bf7233d\\\\\\\",\\\\\\\"should_skip_youth_tos\\\\\\\":false,\\\\\\\"is_youth_regulation_flow_complete\\\\\\\":false,\\\\\\\"is_on_cold_start\\\\\\\":false,\\\\\\\"email_prefilled\\\\\\\":false,\\\\\\\"cp_confirmed_by_auto_conf\\\\\\\":false,\\\\\\\"auto_conf_info\\\\\\\":null,\\\\\\\"in_sowa_experiment\\\\\\\":false,\\\\\\\"youth_regulation_config\\\\\\\":null,\\\\\\\"conf_allow_back_nav_after_change_cp\\\\\\\":null,\\\\\\\"conf_bouncing_cliff_screen_type\\\\\\\":null,\\\\\\\"conf_show_bouncing_cliff\\\\\\\":null,\\\\\\\"eligible_to_flash_call_in_ig4a\\\\\\\":false,\\\\\\\"flash_call_permissions_status\\\\\\\":null,\\\\\\\"attestation_result\\\\\\\":null,\\\\\\\"request_data_and_challenge_nonce_string\\\\\\\":null,\\\\\\\"confirmed_cp_and_code\\\\\\\":null,\\\\\\\"notification_callback_id\\\\\\\":null,\\\\\\\"reg_suma_state\\\\\\\":0,\\\\\\\"is_msplit_neutral_choice\\\\\\\":false,\\\\\\\"msg_previous_cp\\\\\\\":null,\\\\\\\"ntp_import_source_info\\\\\\\":null,\\\\\\\"youth_consent_decision_time\\\\\\\":null,\\\\\\\"username_screen_experience\\\\\\\":\\\\\\\"control\\\\\\\",\\\\\\\"reduced_tos_test_group\\\\\\\":\\\\\\\"control\\\\\\\",\\\\\\\"should_show_spi_before_conf\\\\\\\":true,\\\\\\\"google_oauth_account\\\\\\\":null,\\\\\\\"is_reg_request_from_ig_suma\\\\\\\":false,\\\\\\\"is_igios_spc_reg\\\\\\\":false,\\\\\\\"device_emails\\\\\\\":null,\\\\\\\"is_toa_reg\\\\\\\":false,\\\\\\\"is_threads_public\\\\\\\":false,\\\\\\\"spc_import_flow\\\\\\\":false,\\\\\\\"caa_play_integrity_attestation_result\\\\\\\":null,\\\\\\\"flash_call_provider\\\\\\\":null,\\\\\\\"name_prefill_variant\\\\\\\":\\\\\\\"move_cp_perms_up_without_dialog\\\\\\\",\\\\\\\"spc_birthday_input\\\\\\\":false}\\\",\\\"family_device_id\\\":\\\"00776e25-3a07-474d-b1f6-2063f29fa49f\\\",\\\"offline_experiment_group\\\":\\\"caa_iteration_v6_perf_fb_2\\\",\\\"INTERNAL_INFRA_THEME\\\":\\\"harm_f,default,default,harm_f\\\",\\\"access_flow_version\\\":\\\"F2_FLOW\\\",\\\"is_from_logged_in_switcher\\\":0,\\\"current_step\\\":3}}\"}","bloks_versioning_id":"c3cc18230235472b54176a5922f9b91d291342c3a276e2644dbdb9760b96deec","app_id":"com.bloks.www.bloks.caa.reg.gender.async"},"scale":"3","nt_context":{"using_white_navbar":True,"pixel_ratio":3,"is_push_on":True,"styles_id":"e6c6f61b7a86cdf3fa2eaaffa982fbd1","bloks_version":"c3cc18230235472b54176a5922f9b91d291342c3a276e2644dbdb9760b96deec"}}),
			'fb_api_analytics_tags': '["GraphServices"]',
			'client_trace_id': str(uuid.uuid4())
		}
		post = self.ses.post('https://b-graph.facebook.com/graphql', data=data,  headers=self.headers)
		if "Masukkan email" in post.text:
			self.contac_mail()
		else:
			Fail+=1
	
	def contac_mail(self):
		global Fail
		print(f"\remail: {self.email}")
		time.sleep(2)
			# Proxy URL dengan autentikasi
		proxy_url = 'http://7clptii6e4udqdc-session-1pkfwqpz3h-lifetime-2:bp5qcvv0l3iuje8@rp.proxyscrape.com:6060'
		parsed_proxy = urlparse(proxy_url)
		prox = {
			'http': f"{parsed_proxy.scheme}://{parsed_proxy.netloc}",
			'https': f"{parsed_proxy.scheme}://{parsed_proxy.netloc}"
		}
		data = {
			'method': 'post',
			'pretty': False,
			'format': 'json',
			'server_timestamps': True,
			'locale': 'id_ID',
			'purpose': 'fetch',
			'fb_api_req_friendly_name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.reg.async.contactpoint_email.async',
			'fb_api_caller_class': 'graphservice',
			'client_doc_id': '11994080423068421059028841356',
			'variables': json.dumps({"params":{"params":"{\"params\":\"{\\\"client_input_params\\\":{\\\"accounts_list\\\":[],\\\"email_prefilled\\\":0,\\\"confirmed_cp_and_code\\\":{},\\\"family_device_id\\\":\\\"00776e25-3a07-474d-b1f6-2063f29fa49f\\\",\\\"fb_ig_device_id\\\":[],\\\"device_id\\\":\\\"00776e25-3a07-474d-b1f6-2063f29fa49f\\\",\\\"lois_settings\\\":{\\\"lois_token\\\":\\\"\\\",\\\"lara_override\\\":\\\"\\\"},\\\"msg_previous_cp\\\":\\\"\\\",\\\"is_from_device_emails\\\":0,\\\"switch_cp_first_time_loading\\\":1,\\\"email\\\":\\\""+self.email+"\\\",\\\"switch_cp_have_seen_suma\\\":0},\\\"server_params\\\":{\\\"event_request_id\\\":\\\"63c4d691-ab45-412d-be35-e4ca89e6b4b5\\\",\\\"is_from_logged_out\\\":0,\\\"text_input_id\\\":40370280600068,\\\"layered_homepage_experiment_group\\\":null,\\\"device_id\\\":\\\"00776e25-3a07-474d-b1f6-2063f29fa49f\\\",\\\"waterfall_id\\\":\\\"24f9d94d-8ed0-4a0b-9e0c-7f11379c67b3\\\",\\\"INTERNAL__latency_qpl_instance_id\\\":4.0370280600107E13,\\\"flow_info\\\":\\\"{\\\\\\\"flow_name\\\\\\\":\\\\\\\"new_to_family_fb_default\\\\\\\",\\\\\\\"flow_type\\\\\\\":\\\\\\\"ntf\\\\\\\"}\\\",\\\"is_platform_login\\\":0,\\\"INTERNAL__latency_qpl_marker_id\\\":36707139,\\\"reg_info\\\":\\\"{\\\\\\\"first_name\\\\\\\":\\\\\\\""+self.first_name+"\\\\\\\",\\\\\\\"last_name\\\\\\\":\\\\\\\""+self.last_name+"\\\\\\\",\\\\\\\"full_name\\\\\\\":null,\\\\\\\"contactpoint\\\\\\\":null,\\\\\\\"ar_contactpoint\\\\\\\":null,\\\\\\\"contactpoint_type\\\\\\\":null,\\\\\\\"is_using_unified_cp\\\\\\\":null,\\\\\\\"unified_cp_screen_variant\\\\\\\":null,\\\\\\\"is_cp_auto_confirmed\\\\\\\":false,\\\\\\\"is_cp_auto_confirmable\\\\\\\":false,\\\\\\\"confirmation_code\\\\\\\":null,\\\\\\\"birthday\\\\\\\":\\\\\\\""+self.birth_date+"\\\\\\\",\\\\\\\"did_use_age\\\\\\\":false,\\\\\\\"gender\\\\\\\":1,\\\\\\\"use_custom_gender\\\\\\\":false,\\\\\\\"custom_gender\\\\\\\":null,\\\\\\\"encrypted_password\\\\\\\":null,\\\\\\\"username\\\\\\\":null,\\\\\\\"username_prefill\\\\\\\":null,\\\\\\\"fb_conf_source\\\\\\\":null,\\\\\\\"device_id\\\\\\\":\\\\\\\"00776e25-3a07-474d-b1f6-2063f29fa49f\\\\\\\",\\\\\\\"ig4a_qe_device_id\\\\\\\":null,\\\\\\\"family_device_id\\\\\\\":\\\\\\\"00776e25-3a07-474d-b1f6-2063f29fa49f\\\\\\\",\\\\\\\"nta_eligibility_reason\\\\\\\":null,\\\\\\\"ig_nta_test_group\\\\\\\":null,\\\\\\\"user_id\\\\\\\":null,\\\\\\\"safetynet_token\\\\\\\":null,\\\\\\\"safetynet_response\\\\\\\":null,\\\\\\\"machine_id\\\\\\\":null,\\\\\\\"profile_photo\\\\\\\":null,\\\\\\\"profile_photo_id\\\\\\\":null,\\\\\\\"profile_photo_upload_id\\\\\\\":null,\\\\\\\"avatar\\\\\\\":null,\\\\\\\"email_oauth_token_no_contact_perm\\\\\\\":null,\\\\\\\"email_oauth_token\\\\\\\":null,\\\\\\\"email_oauth_tokens\\\\\\\":null,\\\\\\\"should_skip_two_step_conf\\\\\\\":null,\\\\\\\"openid_tokens_for_testing\\\\\\\":null,\\\\\\\"encrypted_msisdn\\\\\\\":null,\\\\\\\"encrypted_msisdn_for_safetynet\\\\\\\":null,\\\\\\\"cached_headers_safetynet_info\\\\\\\":null,\\\\\\\"should_skip_headers_safetynet\\\\\\\":null,\\\\\\\"headers_last_infra_flow_id\\\\\\\":null,\\\\\\\"headers_last_infra_flow_id_safetynet\\\\\\\":null,\\\\\\\"headers_flow_id\\\\\\\":null,\\\\\\\"was_headers_prefill_available\\\\\\\":null,\\\\\\\"sso_enabled\\\\\\\":null,\\\\\\\"existing_accounts\\\\\\\":null,\\\\\\\"used_ig_birthday\\\\\\\":null,\\\\\\\"sync_info\\\\\\\":null,\\\\\\\"create_new_to_app_account\\\\\\\":null,\\\\\\\"skip_session_info\\\\\\\":null,\\\\\\\"ck_error\\\\\\\":null,\\\\\\\"ck_id\\\\\\\":null,\\\\\\\"ck_nonce\\\\\\\":null,\\\\\\\"should_save_password\\\\\\\":null,\\\\\\\"horizon_synced_username\\\\\\\":null,\\\\\\\"fb_access_token\\\\\\\":null,\\\\\\\"horizon_synced_profile_pic\\\\\\\":null,\\\\\\\"is_identity_synced\\\\\\\":false,\\\\\\\"is_msplit_reg\\\\\\\":null,\\\\\\\"user_id_of_msplit_creator\\\\\\\":null,\\\\\\\"dma_data_combination_consent_given\\\\\\\":null,\\\\\\\"xapp_accounts\\\\\\\":null,\\\\\\\"fb_device_id\\\\\\\":null,\\\\\\\"fb_machine_id\\\\\\\":null,\\\\\\\"ig_device_id\\\\\\\":null,\\\\\\\"ig_machine_id\\\\\\\":null,\\\\\\\"should_skip_nta_upsell\\\\\\\":null,\\\\\\\"big_blue_token\\\\\\\":null,\\\\\\\"skip_sync_step_nta\\\\\\\":null,\\\\\\\"caa_reg_flow_source\\\\\\\":\\\\\\\"login_home_native_integration_point\\\\\\\",\\\\\\\"ig_authorization_token\\\\\\\":null,\\\\\\\"full_sheet_flow\\\\\\\":false,\\\\\\\"crypted_user_id\\\\\\\":null,\\\\\\\"is_caa_perf_enabled\\\\\\\":true,\\\\\\\"is_preform\\\\\\\":true,\\\\\\\"ignore_suma_check\\\\\\\":false,\\\\\\\"ignore_existing_login\\\\\\\":false,\\\\\\\"ignore_existing_login_from_suma\\\\\\\":false,\\\\\\\"ignore_existing_login_after_errors\\\\\\\":false,\\\\\\\"suggested_first_name\\\\\\\":null,\\\\\\\"suggested_last_name\\\\\\\":null,\\\\\\\"suggested_full_name\\\\\\\":null,\\\\\\\"replace_id_sync_variant\\\\\\\":null,\\\\\\\"is_redirect_from_nta_replace_id_sync_variant\\\\\\\":false,\\\\\\\"frl_authorization_token\\\\\\\":null,\\\\\\\"post_form_errors\\\\\\\":null,\\\\\\\"skip_step_without_errors\\\\\\\":false,\\\\\\\"existing_account_exact_match_checked\\\\\\\":false,\\\\\\\"existing_account_fuzzy_match_checked\\\\\\\":false,\\\\\\\"confirmation_code_send_error\\\\\\\":null,\\\\\\\"is_too_young\\\\\\\":false,\\\\\\\"source_account_type\\\\\\\":null,\\\\\\\"whatsapp_installed_on_client\\\\\\\":false,\\\\\\\"confirmation_medium\\\\\\\":null,\\\\\\\"source_credentials_type\\\\\\\":null,\\\\\\\"source_cuid\\\\\\\":null,\\\\\\\"source_account_reg_info\\\\\\\":null,\\\\\\\"soap_creation_source\\\\\\\":null,\\\\\\\"source_account_type_to_reg_info\\\\\\\":null,\\\\\\\"registration_flow_id\\\\\\\":\\\\\\\"b6199014-914d-4e11-8729-d4078bf7233d\\\\\\\",\\\\\\\"should_skip_youth_tos\\\\\\\":false,\\\\\\\"is_youth_regulation_flow_complete\\\\\\\":false,\\\\\\\"is_on_cold_start\\\\\\\":false,\\\\\\\"email_prefilled\\\\\\\":false,\\\\\\\"cp_confirmed_by_auto_conf\\\\\\\":false,\\\\\\\"auto_conf_info\\\\\\\":null,\\\\\\\"in_sowa_experiment\\\\\\\":false,\\\\\\\"youth_regulation_config\\\\\\\":null,\\\\\\\"conf_allow_back_nav_after_change_cp\\\\\\\":null,\\\\\\\"conf_bouncing_cliff_screen_type\\\\\\\":null,\\\\\\\"conf_show_bouncing_cliff\\\\\\\":null,\\\\\\\"eligible_to_flash_call_in_ig4a\\\\\\\":false,\\\\\\\"flash_call_permissions_status\\\\\\\":null,\\\\\\\"attestation_result\\\\\\\":null,\\\\\\\"request_data_and_challenge_nonce_string\\\\\\\":null,\\\\\\\"confirmed_cp_and_code\\\\\\\":null,\\\\\\\"notification_callback_id\\\\\\\":null,\\\\\\\"reg_suma_state\\\\\\\":0,\\\\\\\"is_msplit_neutral_choice\\\\\\\":false,\\\\\\\"msg_previous_cp\\\\\\\":null,\\\\\\\"ntp_import_source_info\\\\\\\":null,\\\\\\\"youth_consent_decision_time\\\\\\\":null,\\\\\\\"username_screen_experience\\\\\\\":\\\\\\\"control\\\\\\\",\\\\\\\"reduced_tos_test_group\\\\\\\":\\\\\\\"control\\\\\\\",\\\\\\\"should_show_spi_before_conf\\\\\\\":true,\\\\\\\"google_oauth_account\\\\\\\":null,\\\\\\\"is_reg_request_from_ig_suma\\\\\\\":false,\\\\\\\"is_igios_spc_reg\\\\\\\":false,\\\\\\\"device_emails\\\\\\\":null,\\\\\\\"is_toa_reg\\\\\\\":false,\\\\\\\"is_threads_public\\\\\\\":false,\\\\\\\"spc_import_flow\\\\\\\":false,\\\\\\\"caa_play_integrity_attestation_result\\\\\\\":null,\\\\\\\"flash_call_provider\\\\\\\":null,\\\\\\\"name_prefill_variant\\\\\\\":\\\\\\\"move_cp_perms_up_without_dialog\\\\\\\",\\\\\\\"spc_birthday_input\\\\\\\":false}\\\",\\\"family_device_id\\\":\\\"00776e25-3a07-474d-b1f6-2063f29fa49f\\\",\\\"offline_experiment_group\\\":\\\"caa_iteration_v6_perf_fb_2\\\",\\\"cp_funnel\\\":0,\\\"INTERNAL_INFRA_THEME\\\":\\\"harm_f,default,default,harm_f\\\",\\\"cp_source\\\":0,\\\"access_flow_version\\\":\\\"F2_FLOW\\\",\\\"is_from_logged_in_switcher\\\":0,\\\"current_step\\\":4}}\"}","bloks_versioning_id":"c3cc18230235472b54176a5922f9b91d291342c3a276e2644dbdb9760b96deec","app_id":"com.bloks.www.bloks.caa.reg.async.contactpoint_email.async"},"scale":"3","nt_context":{"using_white_navbar":True,"pixel_ratio":3,"is_push_on":True,"styles_id":"e6c6f61b7a86cdf3fa2eaaffa982fbd1","bloks_version":"c3cc18230235472b54176a5922f9b91d291342c3a276e2644dbdb9760b96deec"}}),
			'fb_api_analytics_tags': '["GraphServices"]',
			'client_trace_id': str(uuid.uuid4())
		}
		post = self.ses.post('https://b-graph.facebook.com/graphql', data=data,  headers=self.headers,proxies=prox)
		if "Buat kata sandi" in post.text:
			self.createpassword()
		else:
			Fail+=1
	
	def createpassword(self):
		global Fail
		self.enpas = '#PWD_FB4A:0:{}:{}'.format(int(time.time()), self.password)
		print(f"\rbuat password              ", end = '')
			# Proxy URL dengan autentikasi
		proxy_url = 'http://7clptii6e4udqdc-session-1pkfwqpz3h-lifetime-2:bp5qcvv0l3iuje8@rp.proxyscrape.com:6060'
		parsed_proxy = urlparse(proxy_url)
		prox = {
			'http': f"{parsed_proxy.scheme}://{parsed_proxy.netloc}",
			'https': f"{parsed_proxy.scheme}://{parsed_proxy.netloc}"
		}
		data = {
			'method': 'post',
			'pretty': False,
			'format': 'json',
			'server_timestamps': True,
			'locale': 'id_ID',
			'purpose': 'fetch',
			'fb_api_req_friendly_name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.reg.password.async',
			'fb_api_caller_class': 'graphservice',
			'client_doc_id': '11994080423068421059028841356',
			'variables': json.dumps({"params":{"params":"{\"params\":\"{\\\"client_input_params\\\":{\\\"safetynet_response\\\":\\\"\\\",\\\"email_oauth_token_map\\\":{},\\\"caa_play_integrity_attestation_result\\\":\\\"\\\",\\\"fb_ig_device_id\\\":[],\\\"safetynet_token\\\":\\\"\\\",\\\"encrypted_msisdn_for_safetynet\\\":\\\"\\\",\\\"lois_settings\\\":{\\\"lois_token\\\":\\\"\\\",\\\"lara_override\\\":\\\"\\\"},\\\"whatsapp_installed_on_client\\\":1,\\\"machine_id\\\":\\\"\\\",\\\"headers_last_infra_flow_id_safetynet\\\":\\\"\\\",\\\"encrypted_password\\\":\\\""+self.enpas+"\\\"},\\\"server_params\\\":{\\\"event_request_id\\\":\\\"d26c07cb-e1cb-4979-9a18-b2d8b48e9828\\\",\\\"is_from_logged_out\\\":0,\\\"layered_homepage_experiment_group\\\":null,\\\"device_id\\\":\\\"00776e25-3a07-474d-b1f6-2063f29fa49f\\\",\\\"waterfall_id\\\":\\\"24f9d94d-8ed0-4a0b-9e0c-7f11379c67b3\\\",\\\"INTERNAL__latency_qpl_instance_id\\\":4.0382845900211E13,\\\"flow_info\\\":\\\"{\\\\\\\"flow_name\\\\\\\":\\\\\\\"new_to_family_fb_default\\\\\\\",\\\\\\\"flow_type\\\\\\\":\\\\\\\"ntf\\\\\\\"}\\\",\\\"is_platform_login\\\":0,\\\"INTERNAL__latency_qpl_marker_id\\\":36707139,\\\"reg_info\\\":\\\"{\\\\\\\"first_name\\\\\\\":\\\\\\\""+self.first_name+"\\\\\\\",\\\\\\\"last_name\\\\\\\":\\\\\\\""+self.last_name+"\\\\\\\",\\\\\\\"full_name\\\\\\\":null,\\\\\\\"contactpoint\\\\\\\":\\\\\\\""+self.email+"\\\\\\\",\\\\\\\"ar_contactpoint\\\\\\\":null,\\\\\\\"contactpoint_type\\\\\\\":\\\\\\\"email\\\\\\\",\\\\\\\"is_using_unified_cp\\\\\\\":false,\\\\\\\"unified_cp_screen_variant\\\\\\\":null,\\\\\\\"is_cp_auto_confirmed\\\\\\\":false,\\\\\\\"is_cp_auto_confirmable\\\\\\\":false,\\\\\\\"confirmation_code\\\\\\\":null,\\\\\\\"birthday\\\\\\\":\\\\\\\""+self.birth_date+"\\\\\\\",\\\\\\\"did_use_age\\\\\\\":false,\\\\\\\"gender\\\\\\\":1,\\\\\\\"use_custom_gender\\\\\\\":false,\\\\\\\"custom_gender\\\\\\\":null,\\\\\\\"encrypted_password\\\\\\\":null,\\\\\\\"username\\\\\\\":null,\\\\\\\"username_prefill\\\\\\\":null,\\\\\\\"fb_conf_source\\\\\\\":null,\\\\\\\"device_id\\\\\\\":\\\\\\\"00776e25-3a07-474d-b1f6-2063f29fa49f\\\\\\\",\\\\\\\"ig4a_qe_device_id\\\\\\\":null,\\\\\\\"family_device_id\\\\\\\":\\\\\\\"00776e25-3a07-474d-b1f6-2063f29fa49f\\\\\\\",\\\\\\\"nta_eligibility_reason\\\\\\\":null,\\\\\\\"ig_nta_test_group\\\\\\\":null,\\\\\\\"user_id\\\\\\\":null,\\\\\\\"safetynet_token\\\\\\\":null,\\\\\\\"safetynet_response\\\\\\\":null,\\\\\\\"machine_id\\\\\\\":null,\\\\\\\"profile_photo\\\\\\\":null,\\\\\\\"profile_photo_id\\\\\\\":null,\\\\\\\"profile_photo_upload_id\\\\\\\":null,\\\\\\\"avatar\\\\\\\":null,\\\\\\\"email_oauth_token_no_contact_perm\\\\\\\":null,\\\\\\\"email_oauth_token\\\\\\\":null,\\\\\\\"email_oauth_tokens\\\\\\\":null,\\\\\\\"should_skip_two_step_conf\\\\\\\":null,\\\\\\\"openid_tokens_for_testing\\\\\\\":null,\\\\\\\"encrypted_msisdn\\\\\\\":null,\\\\\\\"encrypted_msisdn_for_safetynet\\\\\\\":null,\\\\\\\"cached_headers_safetynet_info\\\\\\\":null,\\\\\\\"should_skip_headers_safetynet\\\\\\\":null,\\\\\\\"headers_last_infra_flow_id\\\\\\\":null,\\\\\\\"headers_last_infra_flow_id_safetynet\\\\\\\":null,\\\\\\\"headers_flow_id\\\\\\\":null,\\\\\\\"was_headers_prefill_available\\\\\\\":null,\\\\\\\"sso_enabled\\\\\\\":null,\\\\\\\"existing_accounts\\\\\\\":null,\\\\\\\"used_ig_birthday\\\\\\\":null,\\\\\\\"sync_info\\\\\\\":null,\\\\\\\"create_new_to_app_account\\\\\\\":null,\\\\\\\"skip_session_info\\\\\\\":null,\\\\\\\"ck_error\\\\\\\":null,\\\\\\\"ck_id\\\\\\\":null,\\\\\\\"ck_nonce\\\\\\\":null,\\\\\\\"should_save_password\\\\\\\":null,\\\\\\\"horizon_synced_username\\\\\\\":null,\\\\\\\"fb_access_token\\\\\\\":null,\\\\\\\"horizon_synced_profile_pic\\\\\\\":null,\\\\\\\"is_identity_synced\\\\\\\":false,\\\\\\\"is_msplit_reg\\\\\\\":null,\\\\\\\"user_id_of_msplit_creator\\\\\\\":null,\\\\\\\"dma_data_combination_consent_given\\\\\\\":null,\\\\\\\"xapp_accounts\\\\\\\":null,\\\\\\\"fb_device_id\\\\\\\":null,\\\\\\\"fb_machine_id\\\\\\\":null,\\\\\\\"ig_device_id\\\\\\\":null,\\\\\\\"ig_machine_id\\\\\\\":null,\\\\\\\"should_skip_nta_upsell\\\\\\\":null,\\\\\\\"big_blue_token\\\\\\\":null,\\\\\\\"skip_sync_step_nta\\\\\\\":null,\\\\\\\"caa_reg_flow_source\\\\\\\":\\\\\\\"login_home_native_integration_point\\\\\\\",\\\\\\\"ig_authorization_token\\\\\\\":null,\\\\\\\"full_sheet_flow\\\\\\\":false,\\\\\\\"crypted_user_id\\\\\\\":null,\\\\\\\"is_caa_perf_enabled\\\\\\\":true,\\\\\\\"is_preform\\\\\\\":true,\\\\\\\"ignore_suma_check\\\\\\\":false,\\\\\\\"ignore_existing_login\\\\\\\":false,\\\\\\\"ignore_existing_login_from_suma\\\\\\\":false,\\\\\\\"ignore_existing_login_after_errors\\\\\\\":false,\\\\\\\"suggested_first_name\\\\\\\":null,\\\\\\\"suggested_last_name\\\\\\\":null,\\\\\\\"suggested_full_name\\\\\\\":null,\\\\\\\"replace_id_sync_variant\\\\\\\":null,\\\\\\\"is_redirect_from_nta_replace_id_sync_variant\\\\\\\":false,\\\\\\\"frl_authorization_token\\\\\\\":null,\\\\\\\"post_form_errors\\\\\\\":null,\\\\\\\"skip_step_without_errors\\\\\\\":false,\\\\\\\"existing_account_exact_match_checked\\\\\\\":false,\\\\\\\"existing_account_fuzzy_match_checked\\\\\\\":false,\\\\\\\"confirmation_code_send_error\\\\\\\":null,\\\\\\\"is_too_young\\\\\\\":false,\\\\\\\"source_account_type\\\\\\\":null,\\\\\\\"whatsapp_installed_on_client\\\\\\\":false,\\\\\\\"confirmation_medium\\\\\\\":null,\\\\\\\"source_credentials_type\\\\\\\":null,\\\\\\\"source_cuid\\\\\\\":null,\\\\\\\"source_account_reg_info\\\\\\\":null,\\\\\\\"soap_creation_source\\\\\\\":null,\\\\\\\"source_account_type_to_reg_info\\\\\\\":null,\\\\\\\"registration_flow_id\\\\\\\":\\\\\\\"b6199014-914d-4e11-8729-d4078bf7233d\\\\\\\",\\\\\\\"should_skip_youth_tos\\\\\\\":false,\\\\\\\"is_youth_regulation_flow_complete\\\\\\\":false,\\\\\\\"is_on_cold_start\\\\\\\":false,\\\\\\\"email_prefilled\\\\\\\":false,\\\\\\\"cp_confirmed_by_auto_conf\\\\\\\":false,\\\\\\\"auto_conf_info\\\\\\\":null,\\\\\\\"in_sowa_experiment\\\\\\\":false,\\\\\\\"youth_regulation_config\\\\\\\":null,\\\\\\\"conf_allow_back_nav_after_change_cp\\\\\\\":null,\\\\\\\"conf_bouncing_cliff_screen_type\\\\\\\":null,\\\\\\\"conf_show_bouncing_cliff\\\\\\\":null,\\\\\\\"eligible_to_flash_call_in_ig4a\\\\\\\":false,\\\\\\\"flash_call_permissions_status\\\\\\\":null,\\\\\\\"attestation_result\\\\\\\":null,\\\\\\\"request_data_and_challenge_nonce_string\\\\\\\":null,\\\\\\\"confirmed_cp_and_code\\\\\\\":null,\\\\\\\"notification_callback_id\\\\\\\":null,\\\\\\\"reg_suma_state\\\\\\\":0,\\\\\\\"is_msplit_neutral_choice\\\\\\\":false,\\\\\\\"msg_previous_cp\\\\\\\":null,\\\\\\\"ntp_import_source_info\\\\\\\":null,\\\\\\\"youth_consent_decision_time\\\\\\\":null,\\\\\\\"username_screen_experience\\\\\\\":\\\\\\\"control\\\\\\\",\\\\\\\"reduced_tos_test_group\\\\\\\":\\\\\\\"control\\\\\\\",\\\\\\\"should_show_spi_before_conf\\\\\\\":true,\\\\\\\"google_oauth_account\\\\\\\":null,\\\\\\\"is_reg_request_from_ig_suma\\\\\\\":false,\\\\\\\"is_igios_spc_reg\\\\\\\":false,\\\\\\\"device_emails\\\\\\\":null,\\\\\\\"is_toa_reg\\\\\\\":false,\\\\\\\"is_threads_public\\\\\\\":false,\\\\\\\"spc_import_flow\\\\\\\":false,\\\\\\\"caa_play_integrity_attestation_result\\\\\\\":null,\\\\\\\"flash_call_provider\\\\\\\":null,\\\\\\\"name_prefill_variant\\\\\\\":\\\\\\\"move_cp_perms_up_without_dialog\\\\\\\",\\\\\\\"spc_birthday_input\\\\\\\":false}\\\",\\\"family_device_id\\\":\\\"00776e25-3a07-474d-b1f6-2063f29fa49f\\\",\\\"offline_experiment_group\\\":\\\"caa_iteration_v6_perf_fb_2\\\",\\\"INTERNAL_INFRA_THEME\\\":\\\"harm_f,default,default,harm_f\\\",\\\"access_flow_version\\\":\\\"F2_FLOW\\\",\\\"is_from_logged_in_switcher\\\":0,\\\"current_step\\\":5}}\"}","bloks_versioning_id":"c3cc18230235472b54176a5922f9b91d291342c3a276e2644dbdb9760b96deec","app_id":"com.bloks.www.bloks.caa.reg.password.async"},"scale":"3","nt_context":{"using_white_navbar":True,"pixel_ratio":3,"is_push_on":True,"styles_id":"e6c6f61b7a86cdf3fa2eaaffa982fbd1","bloks_version":"c3cc18230235472b54176a5922f9b91d291342c3a276e2644dbdb9760b96deec"}}),
			'fb_api_analytics_tags': '["GraphServices"]',
			'client_trace_id': str(uuid.uuid4())
		}
		post = self.ses.post('https://b-graph.facebook.com/graphql', data=data,  headers=self.headers,proxies=prox)
		if "Setujui ketentuan dan kebijakan Facebook" in post.text:
			self.create_account()
		else:
			Fail+=1
	
	def create_account(self):
		global Cp
		print(f"\rsedang konfirmasi akun            ", end = '')
			# Proxy URL dengan autentikasi
		proxy_url = 'http://7clptii6e4udqdc-session-1pkfwqpz3h-lifetime-2:bp5qcvv0l3iuje8@rp.proxyscrape.com:6060'
		parsed_proxy = urlparse(proxy_url)
		prox = {
			'http': f"{parsed_proxy.scheme}://{parsed_proxy.netloc}",
			'https': f"{parsed_proxy.scheme}://{parsed_proxy.netloc}"
		}
		data = {
			'method': 'post',
			'pretty': False,
			'format': 'json',
			'server_timestamps': True,
			'locale': 'id_ID',
			'purpose': 'fetch',
			'fb_api_req_friendly_name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.reg.create.account.async',
			'fb_api_caller_class': 'graphservice',
			'client_doc_id': '11994080423068421059028841356',
			'variables': json.dumps({"params":{"params":"{\"params\":\"{\\\"client_input_params\\\":{\\\"ck_error\\\":\\\"\\\",\\\"device_id\\\":\\\""+str(uuid.uuid4())+"\\\",\\\"ck_nonce\\\":\\\"\\\",\\\"lois_settings\\\":{\\\"lois_token\\\":\\\"\\\",\\\"lara_override\\\":\\\"\\\"},\\\"waterfall_id\\\":\\\""+str(uuid.uuid4())+"\\\",\\\"ck_id\\\":\\\"\\\",\\\"no_contact_perm_email_oauth_token\\\":\\\"\\\",\\\"headers_last_infra_flow_id\\\":\\\"\\\",\\\"machine_id\\\":\\\"\\\",\\\"should_ignore_existing_login\\\":0,\\\"reached_from_tos_screen\\\":1,\\\"encrypted_msisdn\\\":\\\"\\\"},\\\"server_params\\\":{\\\"event_request_id\\\":\\\""+str(uuid.uuid4())+"\\\",\\\"is_from_logged_out\\\":0,\\\"layered_homepage_experiment_group\\\":null,\\\"device_id\\\":\\\""+str(uuid.uuid4())+"\\\",\\\"waterfall_id\\\":\\\""+str(uuid.uuid4())+"\\\",\\\"INTERNAL__latency_qpl_instance_id\\\":4.0399274600152E13,\\\"flow_info\\\":\\\"{\\\\\\\"flow_name\\\\\\\":\\\\\\\"new_to_family_fb_default\\\\\\\",\\\\\\\"flow_type\\\\\\\":\\\\\\\"ntf\\\\\\\"}\\\",\\\"is_platform_login\\\":0,\\\"INTERNAL__latency_qpl_marker_id\\\":36707139,\\\"reg_info\\\":\\\"{\\\\\\\"first_name\\\\\\\":\\\\\\\""+self.first_name+"\\\\\\\",\\\\\\\"last_name\\\\\\\":\\\\\\\""+self.last_name+"\\\\\\\",\\\\\\\"full_name\\\\\\\":null,\\\\\\\"contactpoint\\\\\\\":\\\\\\\""+self.email+"\\\\\\\",\\\\\\\"ar_contactpoint\\\\\\\":null,\\\\\\\"contactpoint_type\\\\\\\":\\\\\\\"email\\\\\\\",\\\\\\\"is_using_unified_cp\\\\\\\":false,\\\\\\\"unified_cp_screen_variant\\\\\\\":null,\\\\\\\"is_cp_auto_confirmed\\\\\\\":false,\\\\\\\"is_cp_auto_confirmable\\\\\\\":false,\\\\\\\"confirmation_code\\\\\\\":null,\\\\\\\"birthday\\\\\\\":\\\\\\\""+self.birth_date+"\\\\\\\",\\\\\\\"did_use_age\\\\\\\":false,\\\\\\\"gender\\\\\\\":1,\\\\\\\"use_custom_gender\\\\\\\":false,\\\\\\\"custom_gender\\\\\\\":null,\\\\\\\"encrypted_password\\\\\\\":\\\\\\\""+self.enpas+"\\\\\\\",\\\\\\\"username\\\\\\\":null,\\\\\\\"username_prefill\\\\\\\":null,\\\\\\\"fb_conf_source\\\\\\\":null,\\\\\\\"device_id\\\\\\\":\\\\\\\""+str(uuid.uuid4())+"\\\\\\\",\\\\\\\"ig4a_qe_device_id\\\\\\\":null,\\\\\\\"family_device_id\\\\\\\":\\\\\\\""+str(uuid.uuid4())+"\\\\\\\",\\\\\\\"nta_eligibility_reason\\\\\\\":null,\\\\\\\"ig_nta_test_group\\\\\\\":null,\\\\\\\"user_id\\\\\\\":null,\\\\\\\"safetynet_token\\\\\\\":null,\\\\\\\"safetynet_response\\\\\\\":null,\\\\\\\"machine_id\\\\\\\":null,\\\\\\\"profile_photo\\\\\\\":null,\\\\\\\"profile_photo_id\\\\\\\":null,\\\\\\\"profile_photo_upload_id\\\\\\\":null,\\\\\\\"avatar\\\\\\\":null,\\\\\\\"email_oauth_token_no_contact_perm\\\\\\\":null,\\\\\\\"email_oauth_token\\\\\\\":null,\\\\\\\"email_oauth_tokens\\\\\\\":[],\\\\\\\"should_skip_two_step_conf\\\\\\\":null,\\\\\\\"openid_tokens_for_testing\\\\\\\":null,\\\\\\\"encrypted_msisdn\\\\\\\":null,\\\\\\\"encrypted_msisdn_for_safetynet\\\\\\\":null,\\\\\\\"cached_headers_safetynet_info\\\\\\\":null,\\\\\\\"should_skip_headers_safetynet\\\\\\\":null,\\\\\\\"headers_last_infra_flow_id\\\\\\\":null,\\\\\\\"headers_last_infra_flow_id_safetynet\\\\\\\":null,\\\\\\\"headers_flow_id\\\\\\\":null,\\\\\\\"was_headers_prefill_available\\\\\\\":null,\\\\\\\"sso_enabled\\\\\\\":null,\\\\\\\"existing_accounts\\\\\\\":null,\\\\\\\"used_ig_birthday\\\\\\\":null,\\\\\\\"sync_info\\\\\\\":null,\\\\\\\"create_new_to_app_account\\\\\\\":null,\\\\\\\"skip_session_info\\\\\\\":null,\\\\\\\"ck_error\\\\\\\":null,\\\\\\\"ck_id\\\\\\\":null,\\\\\\\"ck_nonce\\\\\\\":null,\\\\\\\"should_save_password\\\\\\\":true,\\\\\\\"horizon_synced_username\\\\\\\":null,\\\\\\\"fb_access_token\\\\\\\":null,\\\\\\\"horizon_synced_profile_pic\\\\\\\":null,\\\\\\\"is_identity_synced\\\\\\\":false,\\\\\\\"is_msplit_reg\\\\\\\":null,\\\\\\\"user_id_of_msplit_creator\\\\\\\":null,\\\\\\\"dma_data_combination_consent_given\\\\\\\":null,\\\\\\\"xapp_accounts\\\\\\\":null,\\\\\\\"fb_device_id\\\\\\\":null,\\\\\\\"fb_machine_id\\\\\\\":null,\\\\\\\"ig_device_id\\\\\\\":null,\\\\\\\"ig_machine_id\\\\\\\":null,\\\\\\\"should_skip_nta_upsell\\\\\\\":null,\\\\\\\"big_blue_token\\\\\\\":null,\\\\\\\"skip_sync_step_nta\\\\\\\":null,\\\\\\\"caa_reg_flow_source\\\\\\\":\\\\\\\"login_home_native_integration_point\\\\\\\",\\\\\\\"ig_authorization_token\\\\\\\":null,\\\\\\\"full_sheet_flow\\\\\\\":false,\\\\\\\"crypted_user_id\\\\\\\":null,\\\\\\\"is_caa_perf_enabled\\\\\\\":true,\\\\\\\"is_preform\\\\\\\":true,\\\\\\\"ignore_suma_check\\\\\\\":false,\\\\\\\"ignore_existing_login\\\\\\\":false,\\\\\\\"ignore_existing_login_from_suma\\\\\\\":false,\\\\\\\"ignore_existing_login_after_errors\\\\\\\":false,\\\\\\\"suggested_first_name\\\\\\\":null,\\\\\\\"suggested_last_name\\\\\\\":null,\\\\\\\"suggested_full_name\\\\\\\":null,\\\\\\\"replace_id_sync_variant\\\\\\\":null,\\\\\\\"is_redirect_from_nta_replace_id_sync_variant\\\\\\\":false,\\\\\\\"frl_authorization_token\\\\\\\":null,\\\\\\\"post_form_errors\\\\\\\":null,\\\\\\\"skip_step_without_errors\\\\\\\":false,\\\\\\\"existing_account_exact_match_checked\\\\\\\":false,\\\\\\\"existing_account_fuzzy_match_checked\\\\\\\":false,\\\\\\\"confirmation_code_send_error\\\\\\\":null,\\\\\\\"is_too_young\\\\\\\":false,\\\\\\\"source_account_type\\\\\\\":null,\\\\\\\"whatsapp_installed_on_client\\\\\\\":true,\\\\\\\"confirmation_medium\\\\\\\":null,\\\\\\\"source_credentials_type\\\\\\\":null,\\\\\\\"source_cuid\\\\\\\":null,\\\\\\\"source_account_reg_info\\\\\\\":null,\\\\\\\"soap_creation_source\\\\\\\":null,\\\\\\\"source_account_type_to_reg_info\\\\\\\":null,\\\\\\\"registration_flow_id\\\\\\\":\\\\\\\"b6199014-914d-4e11-8729-d4078bf7233d\\\\\\\",\\\\\\\"should_skip_youth_tos\\\\\\\":false,\\\\\\\"is_youth_regulation_flow_complete\\\\\\\":false,\\\\\\\"is_on_cold_start\\\\\\\":false,\\\\\\\"email_prefilled\\\\\\\":false,\\\\\\\"cp_confirmed_by_auto_conf\\\\\\\":false,\\\\\\\"auto_conf_info\\\\\\\":null,\\\\\\\"in_sowa_experiment\\\\\\\":false,\\\\\\\"youth_regulation_config\\\\\\\":null,\\\\\\\"conf_allow_back_nav_after_change_cp\\\\\\\":null,\\\\\\\"conf_bouncing_cliff_screen_type\\\\\\\":null,\\\\\\\"conf_show_bouncing_cliff\\\\\\\":null,\\\\\\\"eligible_to_flash_call_in_ig4a\\\\\\\":false,\\\\\\\"flash_call_permissions_status\\\\\\\":null,\\\\\\\"attestation_result\\\\\\\":null,\\\\\\\"request_data_and_challenge_nonce_string\\\\\\\":null,\\\\\\\"confirmed_cp_and_code\\\\\\\":null,\\\\\\\"notification_callback_id\\\\\\\":null,\\\\\\\"reg_suma_state\\\\\\\":0,\\\\\\\"is_msplit_neutral_choice\\\\\\\":false,\\\\\\\"msg_previous_cp\\\\\\\":null,\\\\\\\"ntp_import_source_info\\\\\\\":null,\\\\\\\"youth_consent_decision_time\\\\\\\":null,\\\\\\\"username_screen_experience\\\\\\\":\\\\\\\"control\\\\\\\",\\\\\\\"reduced_tos_test_group\\\\\\\":\\\\\\\"control\\\\\\\",\\\\\\\"should_show_spi_before_conf\\\\\\\":true,\\\\\\\"google_oauth_account\\\\\\\":null,\\\\\\\"is_reg_request_from_ig_suma\\\\\\\":false,\\\\\\\"is_igios_spc_reg\\\\\\\":false,\\\\\\\"device_emails\\\\\\\":[],\\\\\\\"is_toa_reg\\\\\\\":false,\\\\\\\"is_threads_public\\\\\\\":false,\\\\\\\"spc_import_flow\\\\\\\":false,\\\\\\\"caa_play_integrity_attestation_result\\\\\\\":null,\\\\\\\"flash_call_provider\\\\\\\":null,\\\\\\\"name_prefill_variant\\\\\\\":\\\\\\\"move_cp_perms_up_without_dialog\\\\\\\",\\\\\\\"spc_birthday_input\\\\\\\":false}\\\",\\\"family_device_id\\\":\\\"00776e25-3a07-474d-b1f6-2063f29fa49f\\\",\\\"offline_experiment_group\\\":\\\"caa_iteration_v6_perf_fb_2\\\",\\\"INTERNAL_INFRA_THEME\\\":\\\"harm_f,default,default,harm_f\\\",\\\"access_flow_version\\\":\\\"F2_FLOW\\\",\\\"app_id\\\":0,\\\"is_from_logged_in_switcher\\\":0,\\\"current_step\\\":8}}\"}","bloks_versioning_id":"c3cc18230235472b54176a5922f9b91d291342c3a276e2644dbdb9760b96deec","app_id":"com.bloks.www.bloks.caa.reg.create.account.async"},"scale":"3","nt_context":{"using_white_navbar":True,"pixel_ratio":3,"is_push_on":True,"styles_id":"e6c6f61b7a86cdf3fa2eaaffa982fbd1","bloks_version":"c3cc18230235472b54176a5922f9b91d291342c3a276e2644dbdb9760b96deec"}}),
			'fb_api_analytics_tags': '["GraphServices"]',
			'client_trace_id': str(uuid.uuid4())
		}
		post = self.ses.post('https://b-graph.facebook.com/graphql', data=data,  headers=self.headers).text.replace('\\', '')
		mek = post
# 		print(mek)
		if "session_key" in mek:
			try:
				self.akses_token = re.search('"access_token":"(.*?)"', mek).group(1)
				self.uid = re.search(r'"uid":(\d+)', mek).group(1)
			except:
				self.akses_token = None
				self.uid = None
			self.confirm_code(self.akses_token, self.uid)
		elif "Kami Tidak Bisa Membuat Akun" in mek:
			print("\nemail kena banned atau terkena spam")
		elif "Nama pengguna atau kata sandi tidak valid" in mek:
			Cp+=1
			time.sleep(10)
			print(f"""\rkkoko""")

	def confirm_code(self ,akses_token, uid):
		global Ok
		print(f"\rWait for the verification code to be send 60 seconds", end = '')
		time.sleep(65)
  			
		self.codeh = self.get_code_tempio()
		# print(f"KODE: " + self.codeh, end = '')

		if self.codeh is None:
			print("tidak ada code verifikasi yang masuk keEmail", end = '')
		elif self.codeh.isdigit():

			Ok+=1
			print(f"\nSuccessfully created Facebook account\n{self.first_name} {self.last_name}\nemail: {self.email}\nbirthday: {self.birth_date}\ncode: {self.codeh}")
			with open('data/RegistrasiCode.txt', 'a') as file:
				file.write(f"{self.uid}|{self.email}|{self.codeh}\n")
		else:
			print('gagal verifikasi')
		time.sleep(2)
		headersz = self.headers
		headersz.update({'authorization': f"OAuth {akses_token}",'x-fb-friendly-name': "FbBloksActionRootQuery-com.bloks.www.bloks.caa.reg.confirmation.async"})
		data = {
			'method': 'post',
			'pretty': False,
			'format': 'json',
			'server_timestamps': True,
			'locale': 'id_ID',
			'purpose': 'fetch',
			'fb_api_req_friendly_name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.reg.confirmation.async',
			'fb_api_caller_class': 'graphservice',
			'client_doc_id': '11994080423068421059028841356',
			'variables': json.dumps({"params":{"params":"{\"params\":\"{\\\"client_input_params\\\":{\\\"confirmed_cp_and_code\\\":{},\\\"code\\\":\\\""+self.codeh+"\\\",\\\"fb_ig_device_id\\\":[],\\\"device_id\\\":\\\"00776e25-3a07-474d-b1f6-2063f29fa49f\\\",\\\"lois_settings\\\":{\\\"lois_token\\\":\\\"\\\",\\\"lara_override\\\":\\\"\\\"}},\\\"server_params\\\":{\\\"event_request_id\\\":\\\"5f165ba7-430a-4f04-9cd1-329a29ed9101\\\",\\\"is_from_logged_out\\\":0,\\\"text_input_id\\\":87834730600067,\\\"layered_homepage_experiment_group\\\":null,\\\"device_id\\\":null,\\\"waterfall_id\\\":\\\"4abc7906-070a-4408-bd6f-98116d10c94f\\\",\\\"wa_timer_id\\\":\\\"wa_retriever\\\",\\\"INTERNAL__latency_qpl_instance_id\\\":8.7834730600097E13,\\\"flow_info\\\":\\\"{\\\\\\\"flow_name\\\\\\\":\\\\\\\"new_to_family_fb_default\\\\\\\",\\\\\\\"flow_type\\\\\\\":\\\\\\\"ntf\\\\\\\"}\\\",\\\"is_platform_login\\\":0,\\\"sms_retriever_started_prior_step\\\":0,\\\"INTERNAL__latency_qpl_marker_id\\\":36707139,\\\"reg_info\\\":\\\"{\\\\\\\"contactpoint\\\\\\\":\\\\\\\""+self.email+"\\\\\\\",\\\\\\\"contactpoint_type\\\\\\\":\\\\\\\"email\\\\\\\",\\\\\\\"first_name\\\\\\\":null,\\\\\\\"last_name\\\\\\\":null,\\\\\\\"full_name\\\\\\\":null,\\\\\\\"ar_contactpoint\\\\\\\":null,\\\\\\\"is_using_unified_cp\\\\\\\":null,\\\\\\\"unified_cp_screen_variant\\\\\\\":null,\\\\\\\"is_cp_auto_confirmed\\\\\\\":null,\\\\\\\"is_cp_auto_confirmable\\\\\\\":null,\\\\\\\"confirmation_code\\\\\\\":null,\\\\\\\"birthday\\\\\\\":null,\\\\\\\"did_use_age\\\\\\\":null,\\\\\\\"gender\\\\\\\":null,\\\\\\\"use_custom_gender\\\\\\\":null,\\\\\\\"custom_gender\\\\\\\":null,\\\\\\\"encrypted_password\\\\\\\":null,\\\\\\\"username\\\\\\\":null,\\\\\\\"username_prefill\\\\\\\":null,\\\\\\\"fb_conf_source\\\\\\\":null,\\\\\\\"device_id\\\\\\\":null,\\\\\\\"ig4a_qe_device_id\\\\\\\":null,\\\\\\\"ig_nta_test_group\\\\\\\":null,\\\\\\\"family_device_id\\\\\\\":null,\\\\\\\"nta_eligibility_reason\\\\\\\":null,\\\\\\\"youth_consent_decision_time\\\\\\\":null,\\\\\\\"username_screen_experience\\\\\\\":null,\\\\\\\"user_id\\\\\\\":null,\\\\\\\"safetynet_token\\\\\\\":null,\\\\\\\"safetynet_response\\\\\\\":null,\\\\\\\"machine_id\\\\\\\":null,\\\\\\\"profile_photo\\\\\\\":null,\\\\\\\"profile_photo_id\\\\\\\":null,\\\\\\\"profile_photo_upload_id\\\\\\\":null,\\\\\\\"avatar\\\\\\\":null,\\\\\\\"email_oauth_token_no_contact_perm\\\\\\\":null,\\\\\\\"email_oauth_token\\\\\\\":null,\\\\\\\"email_oauth_tokens\\\\\\\":null,\\\\\\\"should_skip_two_step_conf\\\\\\\":null,\\\\\\\"openid_tokens_for_testing\\\\\\\":null,\\\\\\\"encrypted_msisdn\\\\\\\":null,\\\\\\\"encrypted_msisdn_for_safetynet\\\\\\\":null,\\\\\\\"cached_headers_safetynet_info\\\\\\\":null,\\\\\\\"should_skip_headers_safetynet\\\\\\\":null,\\\\\\\"headers_last_infra_flow_id\\\\\\\":null,\\\\\\\"headers_last_infra_flow_id_safetynet\\\\\\\":null,\\\\\\\"headers_flow_id\\\\\\\":null,\\\\\\\"was_headers_prefill_available\\\\\\\":null,\\\\\\\"sso_enabled\\\\\\\":null,\\\\\\\"existing_accounts\\\\\\\":null,\\\\\\\"used_ig_birthday\\\\\\\":null,\\\\\\\"sync_info\\\\\\\":null,\\\\\\\"create_new_to_app_account\\\\\\\":null,\\\\\\\"skip_session_info\\\\\\\":null,\\\\\\\"ck_error\\\\\\\":null,\\\\\\\"ck_id\\\\\\\":null,\\\\\\\"ck_nonce\\\\\\\":null,\\\\\\\"should_save_password\\\\\\\":null,\\\\\\\"horizon_synced_username\\\\\\\":null,\\\\\\\"fb_access_token\\\\\\\":null,\\\\\\\"horizon_synced_profile_pic\\\\\\\":null,\\\\\\\"is_identity_synced\\\\\\\":null,\\\\\\\"is_msplit_reg\\\\\\\":null,\\\\\\\"user_id_of_msplit_creator\\\\\\\":null,\\\\\\\"dma_data_combination_consent_given\\\\\\\":null,\\\\\\\"xapp_accounts\\\\\\\":null,\\\\\\\"fb_device_id\\\\\\\":null,\\\\\\\"fb_machine_id\\\\\\\":null,\\\\\\\"ig_device_id\\\\\\\":null,\\\\\\\"ig_machine_id\\\\\\\":null,\\\\\\\"should_skip_nta_upsell\\\\\\\":null,\\\\\\\"big_blue_token\\\\\\\":null,\\\\\\\"skip_sync_step_nta\\\\\\\":null,\\\\\\\"caa_reg_flow_source\\\\\\\":null,\\\\\\\"ig_authorization_token\\\\\\\":null,\\\\\\\"full_sheet_flow\\\\\\\":null,\\\\\\\"crypted_user_id\\\\\\\":null,\\\\\\\"is_caa_perf_enabled\\\\\\\":null,\\\\\\\"is_preform\\\\\\\":null,\\\\\\\"ignore_suma_check\\\\\\\":null,\\\\\\\"ignore_existing_login\\\\\\\":null,\\\\\\\"ignore_existing_login_from_suma\\\\\\\":null,\\\\\\\"ignore_existing_login_after_errors\\\\\\\":null,\\\\\\\"suggested_first_name\\\\\\\":null,\\\\\\\"suggested_last_name\\\\\\\":null,\\\\\\\"suggested_full_name\\\\\\\":null,\\\\\\\"replace_id_sync_variant\\\\\\\":null,\\\\\\\"is_redirect_from_nta_replace_id_sync_variant\\\\\\\":null,\\\\\\\"frl_authorization_token\\\\\\\":null,\\\\\\\"post_form_errors\\\\\\\":null,\\\\\\\"skip_step_without_errors\\\\\\\":null,\\\\\\\"existing_account_exact_match_checked\\\\\\\":null,\\\\\\\"existing_account_fuzzy_match_checked\\\\\\\":null,\\\\\\\"confirmation_code_send_error\\\\\\\":null,\\\\\\\"is_too_young\\\\\\\":null,\\\\\\\"source_account_type\\\\\\\":null,\\\\\\\"whatsapp_installed_on_client\\\\\\\":null,\\\\\\\"confirmation_medium\\\\\\\":null,\\\\\\\"source_credentials_type\\\\\\\":null,\\\\\\\"source_cuid\\\\\\\":null,\\\\\\\"source_account_reg_info\\\\\\\":null,\\\\\\\"soap_creation_source\\\\\\\":null,\\\\\\\"source_account_type_to_reg_info\\\\\\\":null,\\\\\\\"registration_flow_id\\\\\\\":null,\\\\\\\"should_skip_youth_tos\\\\\\\":null,\\\\\\\"is_youth_regulation_flow_complete\\\\\\\":null,\\\\\\\"is_on_cold_start\\\\\\\":null,\\\\\\\"email_prefilled\\\\\\\":null,\\\\\\\"cp_confirmed_by_auto_conf\\\\\\\":null,\\\\\\\"auto_conf_info\\\\\\\":null,\\\\\\\"in_sowa_experiment\\\\\\\":null,\\\\\\\"eligible_to_flash_call_in_ig4a\\\\\\\":null,\\\\\\\"youth_regulation_config\\\\\\\":null,\\\\\\\"conf_allow_back_nav_after_change_cp\\\\\\\":null,\\\\\\\"conf_bouncing_cliff_screen_type\\\\\\\":null,\\\\\\\"conf_show_bouncing_cliff\\\\\\\":null,\\\\\\\"is_msplit_neutral_choice\\\\\\\":null,\\\\\\\"msg_previous_cp\\\\\\\":null,\\\\\\\"ntp_import_source_info\\\\\\\":null,\\\\\\\"flash_call_permissions_status\\\\\\\":null,\\\\\\\"attestation_result\\\\\\\":null,\\\\\\\"request_data_and_challenge_nonce_string\\\\\\\":null,\\\\\\\"confirmed_cp_and_code\\\\\\\":null,\\\\\\\"notification_callback_id\\\\\\\":null,\\\\\\\"reg_suma_state\\\\\\\":null,\\\\\\\"reduced_tos_test_group\\\\\\\":null,\\\\\\\"should_show_spi_before_conf\\\\\\\":null,\\\\\\\"google_oauth_account\\\\\\\":null,\\\\\\\"is_reg_request_from_ig_suma\\\\\\\":null,\\\\\\\"is_igios_spc_reg\\\\\\\":null,\\\\\\\"device_emails\\\\\\\":null,\\\\\\\"is_toa_reg\\\\\\\":null,\\\\\\\"is_threads_public\\\\\\\":null,\\\\\\\"spc_import_flow\\\\\\\":null,\\\\\\\"caa_play_integrity_attestation_result\\\\\\\":null,\\\\\\\"flash_call_provider\\\\\\\":null,\\\\\\\"name_prefill_variant\\\\\\\":null,\\\\\\\"spc_birthday_input\\\\\\\":null}\\\",\\\"family_device_id\\\":null,\\\"offline_experiment_group\\\":\\\"caa_iteration_v6_perf_fb_2\\\",\\\"INTERNAL_INFRA_THEME\\\":\\\"harm_f,default,harm_f\\\",\\\"access_flow_version\\\":\\\"F2_FLOW\\\",\\\"is_from_logged_in_switcher\\\":0,\\\"current_step\\\":10}}\"}","bloks_versioning_id":"c3cc18230235472b54176a5922f9b91d291342c3a276e2644dbdb9760b96deec","app_id":"com.bloks.www.bloks.caa.reg.confirmation.async"},"scale":"3","nt_context":{"using_white_navbar":True,"pixel_ratio":3,"is_push_on":True,"styles_id":"e6c6f61b7a86cdf3fa2eaaffa982fbd1","bloks_version":"c3cc18230235472b54176a5922f9b91d291342c3a276e2644dbdb9760b96deec"}}),
			'fb_api_analytics_tags': '["GraphServices"]',
			'client_trace_id': str(uuid.uuid4())
		}
		
		# Proxy URL dengan autentikasi
		proxy_url = 'http://7clptii6e4udqdc-session-1pkfwqpz3h-lifetime-2:bp5qcvv0l3iuje8@rp.proxyscrape.com:6060'
		parsed_proxy = urlparse(proxy_url)
		prox = {
			'http': f"{parsed_proxy.scheme}://{parsed_proxy.netloc}",
			'https': f"{parsed_proxy.scheme}://{parsed_proxy.netloc}"
		}
		
		post = self.ses.post('https://z-m-graph.facebook.com/graphql?_nc_eh=2,d85ef5bf00352a0865447af9d6d491be,ASjZQCp5kdVU7w-_bmZF9p-fNXTgWWnqDLoBp7GsmuIr4ru9aA3pTTfhMS_Ec0LG1zg', data=data,  headers=headersz).text.replace('\\', '')
		if "confirmation_success" in post:
			waktu = datetime.now(pytz.timezone('Asia/Jakarta')).strftime("%d-%m-%Y %H:%M:%S")
			Ok+=1
			print(f"""\rStatus: confirmation_success""")
			with open('data/FBNewAccount.txt', 'a+') as file:
				file.write(f'first_name: {self.first_name}\nlast_name: {self.last_name}\npassword: {self.password}\nemail: {self.email}\ntoken: {akses_token}\n')
			with open('data/FbNewUID1.txt', 'a+') as mek:
				mek.write(f'{uid}|{self.password}|{self.email}\n')
		os.system('python3 nonproxy1.py')
		
			
MainProcess()