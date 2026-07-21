import streamlit as st
from config import YES_NO, yes_no_label

from config import (
    GENDER,
    REGIONS,
    AREA,
    EDUCATION,
    MARITAL_STATUS,
    EMPLOYMENT,
    SMOKER,
    ALCOHOL,
    YES_NO,
    yes_no_label
)

# =====================================================
# PERSONAL INFORMATION
# =====================================================

def personal_information():

    st.markdown("---")
    st.header("📋 Personal Information")

    col1, col2 = st.columns(2)

    with col1:

        age = st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            value=30
        )

        sex = st.selectbox(
            "Gender",
            GENDER
        )

        bmi = st.number_input(
            "BMI",
            value=25.0
        )

        smoker = st.selectbox(
            "Smoker",
            SMOKER
        )

        household_size = st.number_input(
            "Household Size",
            min_value=1,
            value=4
        )

        dependents = st.number_input(
            "Dependents",
            min_value=0,
            value=2
        )

    with col2:

        region = st.selectbox(
            "Region",
            REGIONS
        )

        urban_rural = st.selectbox(
            "Area",
            AREA
        )

        income = st.number_input(
            "Annual Income",
            value=500000
        )

        education = st.selectbox(
            "Education",
            EDUCATION
        )

        marital_status = st.selectbox(
            "Marital Status",
            MARITAL_STATUS
        )

        employment_status = st.selectbox(
            "Employment Status",
            EMPLOYMENT
        )

        alcohol_freq = st.selectbox(
            "Alcohol Frequency",
            ALCOHOL
        )

    return {
        "age": age,
        "sex": sex,
        "bmi": bmi,
        "smoker": smoker,
        "household_size": household_size,
        "dependents": dependents,
        "region": region,
        "urban_rural": urban_rural,
        "income": income,
        "education": education,
        "marital_status": marital_status,
        "employment_status": employment_status,
        "alcohol_freq": alcohol_freq
    }


# =====================================================
# MEDICAL INFORMATION
# =====================================================

def medical_information():

    st.markdown("---")
    st.header("❤️ Medical Information")

    col3, col4 = st.columns(2)

    with col3:

        visits_last_year = st.number_input(
            "Doctor Visits Last Year",
            min_value=0,
            max_value=100,
            value=5
        )

        hospitalizations_last_3yrs = st.number_input(
            "Hospitalizations (Last 3 Years)",
            min_value=0,
            max_value=20,
            value=0
        )

        days_hospitalized_last_3yrs = st.number_input(
            "Days Hospitalized",
            min_value=0,
            max_value=365,
            value=0
        )

        medication_count = st.number_input(
            "Medication Count",
            min_value=0,
            max_value=100,
            value=2
        )

        systolic_bp = st.number_input(
            "Systolic Blood Pressure",
            min_value=70,
            max_value=250,
            value=120
        )

        diastolic_bp = st.number_input(
            "Diastolic Blood Pressure",
            min_value=40,
            max_value=150,
            value=80
        )

    with col4:

        ldl = st.number_input(
            "LDL Cholesterol",
            min_value=20,
            max_value=300,
            value=100
        )

        hba1c = st.number_input(
            "HbA1c",
            min_value=3.0,
            max_value=15.0,
            value=5.5
        )

        chronic_count = st.number_input(
            "Chronic Diseases Count",
            min_value=0,
            max_value=10,
            value=0
        )

        hypertension = st.selectbox(
        "Hypertension",
        YES_NO,
        format_func=yes_no_label
)

        diabetes = st.selectbox(
            "Diabetes",
            YES_NO,
            format_func=yes_no_label
        )

        asthma = st.selectbox(
            "Asthma",
            YES_NO,
            format_func=yes_no_label
        )

        copd = st.selectbox(
            "COPD",
            YES_NO,
            format_func=yes_no_label
        )

    return {
        "visits_last_year": visits_last_year,
        "hospitalizations_last_3yrs": hospitalizations_last_3yrs,
        "days_hospitalized_last_3yrs": days_hospitalized_last_3yrs,
        "medication_count": medication_count,
        "systolic_bp": systolic_bp,
        "diastolic_bp": diastolic_bp,
        "ldl": ldl,
        "hba1c": hba1c,
        "chronic_count": chronic_count,
        "hypertension": hypertension,
        "diabetes": diabetes,
        "asthma": asthma,
        "copd": copd
    }


# =====================================================
# INSURANCE INFORMATION
# =====================================================

def insurance_information():

    st.markdown("---")
    st.header("🛡 Insurance Information")

    col5, col6 = st.columns(2)

    with col5:

        plan_type = st.selectbox(
            "Plan Type",
            ["Basic", "Silver", "Gold", "Premium"]
        )

        network_tier = st.selectbox(
            "Network Tier",
            ["Tier 1", "Tier 2", "Tier 3"]
        )

        deductible = st.number_input(
            "Deductible",
            min_value=0,
            value=1000
        )

        copay = st.number_input(
            "Copay",
            min_value=0,
            value=20
        )

        policy_term_years = st.number_input(
            "Policy Term (Years)",
            min_value=1,
            max_value=30,
            value=5
        )

        policy_changes_last_2yrs = st.number_input(
            "Policy Changes (Last 2 Years)",
            min_value=0,
            max_value=10,
            value=0
        )

    with col6:

        provider_quality = st.slider(
            "Provider Quality",
            1,
            5,
            3
        )

        risk_score = st.number_input(
            "Risk Score",
            min_value=0.0,
            value=50.0
        )

        annual_premium = st.number_input(
            "Annual Premium",
            min_value=0.0,
            value=12000.0
        )

        monthly_premium = st.number_input(
            "Monthly Premium",
            min_value=0.0,
            value=1000.0
        )

        claims_count = st.number_input(
            "Claims Count",
            min_value=0,
            value=0
        )

        avg_claim_amount = st.number_input(
            "Average Claim Amount",
            min_value=0.0,
            value=0.0
        )

        total_claims_paid = st.number_input(
            "Total Claims Paid",
            min_value=0.0,
            value=0.0
        )

    return {
        "plan_type": plan_type,
        "network_tier": network_tier,
        "deductible": deductible,
        "copay": copay,
        "policy_term_years": policy_term_years,
        "policy_changes_last_2yrs": policy_changes_last_2yrs,
        "provider_quality": provider_quality,
        "risk_score": risk_score,
        "annual_premium": annual_premium,
        "monthly_premium": monthly_premium,
        "claims_count": claims_count,
        "avg_claim_amount": avg_claim_amount,
        "total_claims_paid": total_claims_paid
    }

# =====================================================
# PROCEDURES & HEALTH CONDITIONS
# =====================================================

def procedure_information():

    st.markdown("---")
    st.header("🏥 Procedures & Health Conditions")

    col7, col8 = st.columns(2)

    with col7:

        cardiovascular_disease = st.selectbox(
            "Cardiovascular Disease",
            YES_NO,
            format_func=yes_no_label
        )

        cancer_history = st.selectbox(
            "Cancer History",
            YES_NO,
            format_func=yes_no_label
        )

        kidney_disease = st.selectbox(
            "Kidney Disease",
            YES_NO,
            format_func=yes_no_label
        )

        liver_disease = st.selectbox(
            "Liver Disease",
            YES_NO,
            format_func=yes_no_label
        )

        arthritis = st.selectbox(
            "Arthritis",
            YES_NO,
            format_func=yes_no_label
        )

        mental_health = st.selectbox(
            "Mental Health",
            YES_NO,
            format_func=yes_no_label
        )

    with col8:

        proc_imaging_count = st.number_input(
            "Imaging Procedures",
            min_value=0,
            step=1
        )

        proc_surgery_count = st.number_input(
            "Surgery Procedures",
            min_value=0,
            step=1
        )

        proc_physio_count = st.number_input(
            "Physiotherapy Procedures",
            min_value=0,
            step=1
        )

        proc_consult_count = st.number_input(
            "Consultation Procedures",
            min_value=0,
            step=1
        )

        proc_lab_count = st.number_input(
            "Lab Procedures",
            min_value=0,
            step=1
        )

        is_high_risk = st.selectbox(
            "High Risk Patient",
            YES_NO,
            format_func=yes_no_label
        )

        had_major_procedure = st.selectbox(
            "Major Procedure",
            YES_NO,
            format_func=yes_no_label
        )

    return {
        "cardiovascular_disease": cardiovascular_disease,
        "cancer_history": cancer_history,
        "kidney_disease": kidney_disease,
        "liver_disease": liver_disease,
        "arthritis": arthritis,
        "mental_health": mental_health,
        "proc_imaging_count": proc_imaging_count,
        "proc_surgery_count": proc_surgery_count,
        "proc_physio_count": proc_physio_count,
        "proc_consult_count": proc_consult_count,
        "proc_lab_count": proc_lab_count,
        "is_high_risk": is_high_risk,
        "had_major_procedure": had_major_procedure
    }