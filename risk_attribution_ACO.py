# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 13:01:28 2022

@author: manas
"""

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import urllib.request
st.set_page_config(page_title="Member attribution in Risk Based Arrangements", page_icon=":tada:")

header_container = st.container()
#side_container= st.sidebar()
defs_container = st.container()
main_container = st.container()
ref_container = st.container()

with header_container:
	# for example a logo or a image that looks like a website header
	# different levels of text you can include in your app
	st.title("Attribution in risk based arrangements")
	st.subheader("I welcome comments, feedback and opportunity to learn more or collaborate. Tweet @manas8u")
	st.write("Disclaimer: I have written this for clarity and not originality. Many words and sentences are attributed to orginal authors.")

st.sidebar.header("Sections")
st.sidebar.markdown("[Why think about Attribution?](#why-think-about-attribution)")
st.sidebar.markdown("[Goals of attribution](#goals-of-attribution)")
st.sidebar.markdown("[Methods of attribution](#methods-of-attribution)")
st.sidebar.markdown("[ACO Attribution in Medicare](#aco-attribution-in-medicare)")
st.sidebar.markdown("[Attribution in Medicaid](#attribution-in-medicaid)")
st.sidebar.markdown("[Challenges](#challenges)")


with main_container:
    st.subheader("Definition")
    st.write("Attribution is the process of assigning patients to the provider group that will be responsible for delivering their care and that will be held accountable for the cost and quality of that care (Society of Actuaries, 2018).")

    st.subheader("Why think about attribution?")
    st.write("*Relevance*: The more lives you have attributed to your organization, the more relevant ACO/your organization is in the market.")
    st.write("*Regulatory*: Per Centers for Medicare & Medicaid Services (CMS) regulations, Medicare Shared Saving Program (MSSP) Accountable Care Organizations (ACOs) need to have attribution above 5,000 beneficiaries to remain in MSSP program.")
    st.write("*Risk pool*: Larger population base mitigaties variability that is caused by outlying expenditure in risk based arrangements.")
    st.write("*Financial*: Population Health organizations can earn infrastructure investments or performance based incentives which are based on number of attributed members.")
   
    st.subheader("Goals of attribution")
    st.write("1.As many patients as possible are attributed to a clinician for provision of care and who are accountable for quality and cost ('Capture Rate').")
    st.write("2.Ensure buy-in/support from clinicians for 'attribution methodology' of patients whose care, quality and cost they will be accountable for.")
    st.write("There is some tension between these goals.")

    st.subheader("Methods of attribution")
#    urllib.request.urlretrieve('https://github.com/mangospace/ACO_attribution/blob/be7b14c30463dccae292fcaadbd0ad0fca441f57/Screenshot%202022-09-25%20165833.jpg',"image_1.jpg")
#    image1 = Image.open("image_1.jpg")
#    image1.show()
    st.image('https://raw.githubusercontent.com/mangospace/ACO_attribution/be7b14c30463dccae292fcaadbd0ad0fca441f57/Screenshot%202022-09-25%20165833.jpg', caption='Patient Attribution Flow Chart(Health Care Payment Learning and Action Network)')
    st.write("There are three basic methods for attribution:")
    st.write("Patient choice, geographic-based and visit-based.") 
    st.write("Patient choice is the simplest method and relies on patients choosing and indicating which provider they would like to be responsible for their care. This method is most often used in HMOs e.g. Medicare Advantage or Commercial HMOs. However, this method is hard to enforce with low-cost members that skew toward not choosing a provider.")
    st.write("Geographic-based attribution is done through assignment of a network or use of zip code or county of residence. This method can ensure that most members/patients are attributed to a clinician but it lacks the sensitivity for how care is delivered among patients and providers.This is used in Maryland Medicare Performance Adjustment (MPA) and in devising global budgets for rural hospitals. Colorado’s Medicaid program, contracts with ACOs in geographic regions. One potential advantage is that a geographically defined ACO could impact community prevention interventions to address the underlying causes of death and ill-health, such as opiod abuse, and physical inactivity.")
    st.write("Visit-based attribution is an algorithm-based approach that uses claims experience and is used most often in Medicare ACOs e.g. MSSP. This method depends on quality of data e.g. if patients change plans,e.g. Medicaid plans or Commercial to Medicare, a health plan might not be able to correctly attribute patients. Many health entities use a tax identification number to identify providers but those identification numbers can change if the provider is acquired or merged into another entity. Or sometimes clinicians change employers and if patients are not 'handed off' clearly or patients have not seen a new clinician, it can be challenging to attribute patients. Challenges also arise as clinicians and practices can 'discharge patients from their practice' based on their conversation/knowledge of patients e.g. patient living in Long Term Care or patient expressing intent to see another PCP while the payor membership is based exclusively on patients choosing to update their choise in the payor's system. Duration of look back period for counting the visits can improve attribution while also creating some challenges.")

    st.subheader("ACO Attribution in Medicare")
    st.image('https://raw.githubusercontent.com/mangospace/ACO_attribution/main/Screenshot%202022-09-27%20205812.jpg', caption='Attribution in different Medicare ACOs types (Norris, 2020)')
    st.write("In concurrent attribution, patients are assigned based on care provided during the contract year, and final attribution occurs at the end of the contract performance year (PY). In concurrent attribution, patients who received care from the ACO during the Performance Year are captured in the ACO population. Epidemiologists use 'open cohort' for this kind of grouping (CMS, 2018).")
    st.image('https://raw.githubusercontent.com/mangospace/ACO_attribution/main/Concurrent%20Attribution.jpg', caption='Concurrent patient attribution')
    st.write("In prospective attribution, patients are assigned at the start of the contract PY based on claims in the prior calendar year, which allows ACOs to know their defined population and provide care management during the PY (Kaufman et al.).Epidemiologists would call this a 'closed cohort'. A challenge for this approach is that providers remain accountable for the patients on their original list, regardless of whether patients' care patterns over the year suggest they have changed systems. Further, the provider cannot gain formal accountability for new patients during the year, even if those patients’ care patterns identify the provider to be their primary source of care(Shellabarger, 2020).")
    st.image('https://raw.githubusercontent.com/mangospace/ACO_attribution/main/Prospective%20attribution.jpg', caption='Prospective patient attribution')
    st.write("With the Pathways to Success MSSP rule, CMS allows ACOs to choose attribution methodology: concurrent or prospective (potentially supplemented by voluntary patient attribution)")
    st.write("CMS uses following methodology for attributing patients to MSSP ACOs.")
    st.write("For Performance Year (PY) 2018 and subsequent performance years, beneficiaries have the opportunity to designate a primary clinician as responsible for coordinating their overall care. Beneficiaries may make this voluntary alignment through MyMedicare.gov at any time during the year.This voluntary alignment supersedes claims-based assignment. ")
    st.write("For individuals who have not choosen a PCP as described above, CMS uses claims based methodology for attributing patients to ACOs as described in the June 2015 Final Rule.")
    st.write("If a beneficiary receives at least one primary care service from a physician, within a specific ACO, the beneficiary may be assigned to that ACO based on a two-step process.")
    st.write("The first step assigns a beneficiary to an ACO if he or she receives a plurality of primary care services from primary care practitioners (i.e., primary care physicians, nurse practitioners, clinical nurse specialists, physician assistants, or ACO professionals providing services at a FQHC/RHC) within the ACO over last 2 years. CMS defines primary care physicians as physicians with one of the five following specialty designations: internal medicine, general practice, family practice, pediatric medicine, or geriatric medicine")
    st.write("Primary care services include evaluation and management services provided in office and other non-inpatient and non–emergency-room settings, as well as initial Medicare visits and annual wellness visits. If two ACOs/primary care clinicians tie for the largest share of a beneficiary’s primary care services, then the beneficiary is assigned to the TIN that provided primary care services most recently.")
    st.write("For the subset of individuals who have not received primary care services from a primary care physician, non-physician, or ACO professional providing services at a FQHC/RHC inside or outside the ACO, CMS applies the second step. Under this second step, CMS assigns a beneficiary to an ACO if the beneficiary receives the plurality of his or her primary care services from a specialist physician used in assignment within the ACO.")
             
    st.subheader("Attribution in Medicaid")
    st.write("Medicaid programs are run by states and have populations that encompass community dwelling individuals but also individuals living in Long Term Care settings. Objective to attribute patients is meant to not only advance quality and managing care of beneficiaries but sometimes, supplemental and equitable funding for hospitals e.g. DSRIP program in NJ and NY. Therefore, attribution process needs to be viewed through the lens of the intended outcome.")
    st.write("Many Medicaid beneficiaries access primary care through the emergency room (ER), urgent care, or perhaps do not use primary care at all. Because of lack of claims experience, it can be difficult to appropriately attribute a Medicaid beneficiary to a provider who is realistically able to manage the patient’s care. This can be overcome to the extent if hospitals/Urgent Care/Emergency Department (and/or their clinicians) can be part of ACOs/IPAs. Below are some methodologies used in attribution in Medicaid Section 1115 programs.")
    st.image('https://raw.githubusercontent.com/mangospace/ACO_attribution/main/Screenshot%202022-09-29%20100857_1.jpg')
    st.image('https://raw.githubusercontent.com/mangospace/ACO_attribution/main/Screenshot%202022-09-29%20100857_2.jpg', caption='Attribution methods in Section 1115 Medicaid (Source: Au 2017))')

    st.subheader("Challenges")
    st.image('https://raw.githubusercontent.com/mangospace/ACO_attribution/main/Screenshot%202022-09-25%20213505.jpg', caption='Incremental performance of patient attribution methodologies, BCBS - MA, unknown Line of Business (Health Care Payment Learning and Action Network)')
    st.write("As a payor, the definition of attribution should be thoughtful and defensible (vs adhoc for each group or clinician or provider). Any attribution methodology should be respectful of the other/previous aggremenets with other provider groups (e.g. delegation agreements, if they exist).")
    st.write("While payors could be satisfied with 75-80% attribution, this might not be satisfactory to PCPs/risk taking entities for whom 20-25% 'misidentification' can result in significant financial risk (McCoy,2018; Kaufman,2020).")
    st.write("Attribution is best in HMOs where patients have to choose a PCP at the time of enrollment. Even in HMOs, if PCP retires or member switches primary care provider without updating the plan, it can be difficult to resolve attribution from provider perspective.")
    st.write("These challenges can be exacerbated when payors delegate risk for PPO members (who don't have to elect a PCP). Among PPO members and Medicare ACOs with administrative attribution, if a member does not see a PCP but receives care from several specialists, which specialist could the patient be attributed to and how it is communicated with the specialist in timely and transparent manner, remains challenging.") 
    st.write("Change in patterns of care in 2020 and 2021 (due to Covid) can result in distortion in 2020/2021 claims/visit based attribution. Change in telehealth utilization due to Covid can also result in change in attribution unless payors and providers agree to accept telehealth evaluation and management (E&M) codes (Gusland 2020).")
    st.write("Patient mobility in and out of geographies, change of insurance caused by change in eligibility, infrequent healthcare utilization or intensive/exclusive utilization for mental health or emergency department services can make attribution difficult for Medicaid beneficiaries. If you know of patient attribution models that do not fall in the above categories or have found different challenges, as could happen when payors interested in building/supporting new models of care e.g. Virtual/digital care delivery or Care Coordination, I would love to learn from you.")
		
with ref_container:
	# for example a logo or a image that looks like a website header
	# different levels of text you can include in your app
    st.subheader("References")
    st.write('Harker M, Olson A Patient Attribution The Basis for All Value-based Care. Society of Actuaries.(2018) https://www.soa.org/globalassets/assets/Files/resources/research-report/2018/patient-attribution.pdf')
    st.write("Health Care Payment Learning and Action Network, Accelerating and Aligning Population-Based Payment Models: Patient Attribution, HCP-LAN( 2016) http://hcplan.org/workproducts/pa-whitepaper-final.pdf")
    st.write('The Colorado Department of Health Care Policy and Financing. Accountable Care Collaborative. www.colorado.gov/cs/Satellite/HCPF/HCPF/1233759745246')
    st.write("Medicare Shared Savings Program: Shared Savings and Losses and Assigment methodology Specifications (2018) https://www.cms.gov/Medicare/Medicare-Fee-for-Service-Payment/sharedsavingsprogram/Downloads/Shared-Savings-Losses-Assignment-Spec-V6.pdf")
    st.write("Norris C, Jensen B, Grzeskowiak D Direct Contracting: A program summary and comparison with MSSP and NGACO (2020)")
    st.write("Hunt Z, Johnson RL, Larson A Seven key challenges for Medicaid states considering alternative payment models (2019) https://www.milliman.com/en/insight/seven-key-challenges-for-medicaid-states-considering-alternative-payment-models")
    st.write('Shellabarger S, Mills C, Anderson L Prospective and retrospective assignment in MSSP and beyond.(2020) https://www.milliman.com/-/media/milliman/pdfs/articles/prospective-retrospective-assignment-mssp-beyond.ashx')
    st.write('McCoy RG, Bunkers KS, Ramar P, Meier SK, Benetti LL, Nesse RE, Naessens JM. Patient attribution: why the method matters. Am J Manag Care. 2018 Dec;24(12):596-603.https://www.ajmc.com/view/patient-attribution-why-the-method-matters')
    st.write("Kaufman BG, Bleser WK, Saunders R, Anderson D, Van Houtven CH, Muhlestein DB, Clough J, McClellan MB. Prospective or retrospective ACO attribution matters for seriously ill patients. Am J Manag Care. 2020 Dec;26(12):534-540. doi: 10.37765/ajmc.2020.88541.https://www.ajmc.com/view/prospective-or-retrospective-aco-attribution-matters-for-seriously-ill-patients")
    st.write('Gusland C,Larson A, Sweatman BA Ten questions providers should be asking about their value-based contracts and the COVID-19 pandemic. (2020) https://us.milliman.com/en/insight/ten-questions-providers-should-be-asking-about-their-valuebased-contracts-and-the-covid19-pandemic')
    st.write('Au M, Appold C, Stringer R, Balke P Attribution in DSRIP Demonstration Programs: A Spotlight on New Jersey and New York (2017) https://www.medicaid.gov/medicaid/downloads/1115-ib12-508-dsrip-attribution.pdf')
