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
st.set_page_config(page_title="MSSP ACO: Membership attribution", page_icon=":tada:")

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

with main_container:
    st.subheader("Definition")
    st.write("Attribution is the process of assigning patients to the provider group that will be responsible for delivering their care and that will be held accountable for the cost and quality of that care (SOA).")

    st.subheader("Why think about attribution?")
    st.write("*Relevance*: The more lives you have attributed to your organization, the more relevant ACO/your organization is in the market.")
    st.write("*Regulatory*: MSSP ACOs need to stay above 5,000 beneficiaries to even be considered an ACO in MSSP program.")
    st.write("*Risk pool*: Larger population base allows mitigating variability.")
    

    st.subheader("Goals of attribution")
    st.write("1.As many patients as possible are attributed to a clinician for provision of care and accountable for quality and cost ('Capture Rate').")
    st.write("2.Ensure buy-in/support from clinicians about the 'attribution methodology' of patients for whose care and that will be held accountable for the cost and quality of that care.")
    st.write("There is some tension between these goals.")

    st.subheader("Methods of attribution")
#    urllib.request.urlretrieve('https://github.com/mangospace/ACO_attribution/blob/be7b14c30463dccae292fcaadbd0ad0fca441f57/Screenshot%202022-09-25%20165833.jpg',"image_1.jpg")
#    image1 = Image.open("image_1.jpg")
#    image1.show()
    st.image('https://raw.githubusercontent.com/mangospace/ACO_attribution/be7b14c30463dccae292fcaadbd0ad0fca441f57/Screenshot%202022-09-25%20165833.jpg', caption='Patient Attribution Flow Chart(Health Care Payment Learning and Action Network (HCP-LAN)')
    st.write("There are three basic methods for attribution:")
    st.write("Patient choice, geographic-based and visit-based. Patient choice is the simplest method and relies on patients choosing and indicating which provider they would like to be responsible for their care. This method is most often used in HMOs e.g. Medicare Advantage or Commercial HMOs. However, this method is hard to enforce with low-cost members that skew toward not choosing a provider.")
    st.write("Geographic-based attribution is done through assignment of a network or use of zip code or county of residence. This method can ensure that most members/patients are attributed to a clinician but it lacks the sensitivity for how care is delivered among patients and providers.This is used in Maryland Medicare Performance Adjustment (MPA) or in devising global budgets for rural hospitals.")
    st.write("Visit-based attribution is an algorithm-based approach that uses claims experience and is used most often in Medicare ACOs e.g. MSSP. This method depends on quality of data e.g. if patients change plans,e.g. Medicaid plans or Commercial to Medicare, a health plan might not be able to correctly attribute patients. Many health entities use a tax identification number to identify providers but those identification numbers can change if the provider is acquired or merged into another entity. Or sometimes clinicians change employers and if patients are not 'handed off' clearly or patients have not seen a new clinician, it can be challenging to attribute patients. Challenges also arise as clinicians and practices can 'discharge patients from their practice' based on their conversation/knowledge of patients e.g. patient living in Long Term Care or patient expressing intent to see another PCP while the payor membership is based exclusively on patients choosing to update their choise in the payor's system. Duration of look back period for counting the visits can improve attribution while also creating some challenges.")
    st.write("Despite these methods, attribution for Medicaid members can be challenging.")
    st.write("If you know of patient attribution models that do not fall in the above categories, as could happen when payors interested in building/supporting new models of care e.g. Virtual/digital or Care Coordination, I would love to learn.")

    st.subheader("MSSP ACO Attribution")
    st.write("In concurrent attribution, patients are assigned based on care provided during the contract year, and final attribution occurs at the end of the contract performance year (PY). In concurrent attribution, patients who received care from the ACO during the Performance Year are captured in the ACO population. Epidemiologists use 'open cohort' for this kind of grouping.")
    st.write("In prospective attribution, patients are assigned at the start of the contract PY based on claims in the prior calendar year, which allows ACOs to know their defined population and provide care management during the PY (Kaufman et al.).Epidemiologists would call this a 'closed cohort'. A challenge for this approach is that providers remain accountable for the patients on their original list, regardless of whether patients' care patterns over the year suggest they have changed systems. Further, the provider cannot gain formal accountability for new patients during the year, even if those patients’ care patterns identify the provider to be their primary source of care.")
    st.write("With the Pathways to Success MSSP rule, CMS allows ACOs to choose attribution methodology: concurrent or prospective (potentially supplemented by voluntary patient attribution)")
    st.write("CMS uses following methodology for attributing patients to ACOs.")
    st.write("For Performance Year (PY) 2018 and subsequent performance years, beneficiaries have the opportunity to designate a primary clinician as responsible for coordinating their overall care. Beneficiaries may make this voluntary alignment through MyMedicare.gov at any time during the year.This voluntary alignment supersedes claims-based assignment. ")
    st.write("For individuals who have not choosen a PCP, CMS uses following claims based methodology for attributing patients to ACOs as described in the June 2015 Final Rule.")
    st.write("If a beneficiary receives at least one primary care service from a physician, within a specific ACO, the beneficiary may be assigned to that ACO based on a two-step process.")
    st.write("The first step assigns a beneficiary to an ACO if he or she receives a plurality of primary care services from primary care practitioners (i.e., primary care physicians, nurse practitioners, clinical nurse specialists, physician assistants, or ACO professionals providing services at a FQHC/RHC) within the ACO over last 2 years. CMS defines primary care physicians as physicians with one of the five following specialty designations: internal medicine, general practice, family practice, pediatric medicine, or geriatric medicine")
    st.write("Primary care services include evaluation and management services provided in office and other non-inpatient and non–emergency-room settings, as well as initial Medicare visits and annual wellness visits. If two ACOs/primary care clinicians tie for the largest share of a beneficiary’s primary care services, then the beneficiary is assigned to the TIN that provided primary care services most recently.")
    st.write("For the subset of individuals who have not received primary care services from a primary care physician, non-physician, or ACO professional providing services at a FQHC/RHC inside or outside the ACO, CMS applies the second step. Under this second step, CMS assigns a beneficiary to an ACO if the beneficiary receives the plurality of his or her primary care services from a specialist physician used in assignment within the ACO.")
             
with ref_container:
	# for example a logo or a image that looks like a website header
	# different levels of text you can include in your app
    st.subheader("References")
    st.write("Health Care Payment Learning and Action Network (HCP-LAN), Accelerating and Aligning Population-Based Payment Models: Patient Attribution, HCP-LAN, 2016, http://hcplan.org/workproducts/pa-whitepaper-final.pdf. Copyright © 2016 The MITRE Corporation.")
    st.write("Medicare Shared Savings Program: Shared Savings and Losses and Assigment methodology Specifications (2018) https://www.cms.gov/Medicare/Medicare-Fee-for-Service-Payment/sharedsavingsprogram/Downloads/Shared-Savings-Losses-Assignment-Spec-V6.pdf")
    st.write("Kaufman BG, Bleser WK, Saunders R, Anderson D, Van Houtven CH, Muhlestein DB, Clough J, McClellan MB. Prospective or retrospective ACO attribution matters for seriously ill patients. Am J Manag Care. 2020 Dec;26(12):534-540. doi: 10.37765/ajmc.2020.88541.https://www.ajmc.com/view/prospective-or-retrospective-aco-attribution-matters-for-seriously-ill-patients")
    st.write('McCoy RG, Bunkers KS, Ramar P, Meier SK, Benetti LL, Nesse RE, Naessens JM. Patient attribution: why the method matters. Am J Manag Care. 2018 Dec;24(12):596-603.https://www.ajmc.com/view/patient-attribution-why-the-method-matters')
    st.write('Harker M, Olson A Patient Attribution The Basis for All Value-based Care. Society of Actuaries.(2018) https://www.soa.org/globalassets/assets/Files/resources/research-report/2018/patient-attribution.pdf')
