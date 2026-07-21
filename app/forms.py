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


def section_card(icon_title, description):
    """Render a modern section header card."""
    st.markdown("---")
    st.markdown(f"""
    <div style="
        background:#EFF6FF;
        padding:15px;
        border-radius:12px;
        border-left:6px solid #2563eb;
        margin-bottom:20px;
    ">
        <h3 style="margin:0;">{icon_title}</h3>
        <p style="margin:5px 0 0 0;color:#555;">
            {description}
        </p>
    </div>
    """, unsafe_allow_html=True)


# =====================================================
# PERSONAL INFORMATION
# =====================================================

def personal_information():

    section_card(
        "📋 Personal Information",
        "Enter the customer's personal details."
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:

        age = st.number_input(
            "👤 Age",
            min_value=18,
            max_value=100,
            value=30,
            step=1,
            format="%d",
            help="Enter the customer's age."
        )

        sex = st.selectbox(
            "⚧ Gender",
            GENDER,
            help="Select the customer's gender."
        )

        bmi = st.number_input(
            "⚖️ BMI",
            min_value=10.0,
            max_value=60.0,
            value=25.0,
            step=0.1,
            format="%.1f",
            help="Body Mass Index of the customer."
        )

        smoker = st.selectbox(
            "🚬 Smoker",
            SMOKER,
            help="Select the customer's smoking status."
        )

        household_size = st.number_input(
            "👨‍👩‍👧 Household Size",
            min_value=1,
            value=4,
            step=1,
            format="%d",
            help="Total number of people in the household."
        )

        dependents = st.number_input(
            "👶 Dependents",
            min_value=0,
            value=2,
            step=1,
            format="%d",
            help="Number of dependents the customer supports."
        )

    with col2:

        region = st.selectbox(
            "🌍 Region",
            REGIONS,
            help="Select the customer's region."
        )

        urban_rural = st.selectbox(
            "🏠 Area",
            AREA,
            help="Select whether the customer lives in an urban or rural area."
        )

        income = st.number_input(
            "💰 Annual Income",
            min_value=0,
            value=500000,
            step=10000,
            format="%d",
            help="Customer's total annual income."
        )

        education = st.selectbox(
            "🎓 Education",
            EDUCATION,
            help="Select the customer's highest level of education."
        )

        marital_status = st.selectbox(
            "💍 Marital Status",
            MARITAL_STATUS,
            help="Select the customer's marital status."
        )

        employment_status = st.selectbox(
            "💼 Employment Status",
            EMPLOYMENT,
            help="Select the customer's current employment status."
        )

        alcohol_freq = st.selectbox(
            "🍷 Alcohol Frequency",
            ALCOHOL,
            help="How often the customer consumes alcohol."
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

    section_card(
        "❤️ Medical Information",
        "Provide the customer's medical history."
    )

    col3, col4 = st.columns(2, gap="large")

    with col3:

        visits_last_year = st.number_input(
            "👨‍⚕️ Doctor Visits Last Year",
            min_value=0,
            max_value=100,
            value=5,
            step=1,
            format="%d",
            help="Number of doctor visits in the last year."
        )

        hospitalizations_last_3yrs = st.number_input(
            "🏥 Hospitalizations (Last 3 Years)",
            min_value=0,
            max_value=20,
            value=0,
            step=1,
            format="%d",
            help="Number of hospitalizations in the last 3 years."
        )

        days_hospitalized_last_3yrs = st.number_input(
            "🛏️ Days Hospitalized",
            min_value=0,
            max_value=365,
            value=0,
            step=1,
            format="%d",
            help="Total days hospitalized in the last 3 years."
        )

        medication_count = st.number_input(
            "💊 Medications",
            min_value=0,
            max_value=100,
            value=2,
            step=1,
            format="%d",
            help="Number of medications currently taken."
        )

        systolic_bp = st.number_input(
            "❤️ Systolic Blood Pressure",
            min_value=70,
            max_value=250,
            value=120,
            step=1,
            format="%d",
            help="Systolic blood pressure reading (mmHg)."
        )

        diastolic_bp = st.number_input(
            "❤️ Diastolic Blood Pressure",
            min_value=40,
            max_value=150,
            value=80,
            step=1,
            format="%d",
            help="Diastolic blood pressure reading (mmHg)."
        )

    with col4:

        ldl = st.number_input(
            "🩸 LDL Cholesterol",
            min_value=20,
            max_value=300,
            value=100,
            step=1,
            format="%d",
            help="LDL cholesterol level (mg/dL)."
        )

        hba1c = st.number_input(
            "🧪 HbA1c",
            min_value=3.0,
            max_value=15.0,
            value=5.5,
            step=0.1,
            format="%.1f",
            help="HbA1c blood sugar level (%)."
        )

        chronic_count = st.number_input(
            "🩺 Chronic Diseases Count",
            min_value=0,
            max_value=10,
            value=0,
            step=1,
            format="%d",
            help="Number of chronic diseases diagnosed."
        )

        hypertension = st.selectbox(
            "❤️ Hypertension",
            YES_NO,
            format_func=yes_no_label,
            help="Does the customer have hypertension?"
        )

        diabetes = st.selectbox(
            "🍬 Diabetes",
            YES_NO,
            format_func=yes_no_label,
            help="Does the customer have diabetes?"
        )

        asthma = st.selectbox(
            "🌬️ Asthma",
            YES_NO,
            format_func=yes_no_label,
            help="Does the customer have asthma?"
        )

        copd = st.selectbox(
            "🫁 COPD",
            YES_NO,
            format_func=yes_no_label,
            help="Does the customer have COPD?"
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

    section_card(
        "🛡 Insurance Information",
        "Enter the customer's insurance plan and claims details."
    )

    col5, col6 = st.columns(2, gap="large")

    with col5:

        plan_type = st.selectbox(
            "📄 Plan Type",
            ["Basic", "Silver", "Gold", "Premium"],
            help="Select the insurance plan type."
        )

        network_tier = st.selectbox(
            "🌐 Network Tier",
            ["Tier 1", "Tier 2", "Tier 3"],
            help="Select the provider network tier."
        )

        deductible = st.number_input(
            "💰 Deductible",
            min_value=0,
            value=1000,
            step=100,
            format="%d",
            help="Annual deductible amount."
        )

        copay = st.number_input(
            "💳 Copay",
            min_value=0,
            value=20,
            step=5,
            format="%d",
            help="Fixed copay amount per visit."
        )

        policy_term_years = st.number_input(
            "📅 Policy Term (Years)",
            min_value=1,
            max_value=30,
            value=5,
            step=1,
            format="%d",
            help="Length of the policy term in years."
        )

        policy_changes_last_2yrs = st.number_input(
            "🔄 Policy Changes (Last 2 Years)",
            min_value=0,
            max_value=10,
            value=0,
            step=1,
            format="%d",
            help="Number of policy changes in the last 2 years."
        )

    with col6:

        provider_quality = st.slider(
            "⭐ Provider Quality",
            min_value=1,
            max_value=5,
            value=3,
            help="Rate the provider quality from 1 (poor) to 5 (excellent)."
        )

        risk_score = st.number_input(
            "📊 Risk Score",
            min_value=0.0,
            max_value=100.0,
            value=50.0,
            step=1.0,
            help="Overall risk score of the customer."
        )

        annual_premium = st.number_input(
            "💵 Annual Premium",
            min_value=0.0,
            value=12000.0,
            step=500.0,
            help="Total annual premium amount."
        )

        monthly_premium = st.number_input(
            "💳 Monthly Premium",
            min_value=0.0,
            value=1000.0,
            step=100.0,
            help="Monthly premium amount."
        )

        claims_count = st.number_input(
            "📑 Claims Count",
            min_value=0,
            value=0,
            step=1,
            format="%d",
            help="Total number of claims filed."
        )

        avg_claim_amount = st.number_input(
            "📈 Average Claim Amount",
            min_value=0.0,
            value=0.0,
            step=100.0,
            help="Average amount per claim."
        )

        total_claims_paid = st.number_input(
            "💸 Total Claims Paid",
            min_value=0.0,
            value=0.0,
            step=100.0,
            help="Total amount paid out in claims."
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

    section_card(
        "🏥 Procedures & Health Conditions",
        "Provide details on past procedures and existing health conditions."
    )

    col7, col8 = st.columns(2, gap="large")

    with col7:

        cardiovascular_disease = st.selectbox(
            "❤️ Cardiovascular Disease",
            YES_NO,
            format_func=yes_no_label,
            help="Does the customer have cardiovascular disease?"
        )

        cancer_history = st.selectbox(
            "🎗️ Cancer History",
            YES_NO,
            format_func=yes_no_label,
            help="Does the customer have a history of cancer?"
        )

        kidney_disease = st.selectbox(
            "🩺 Kidney Disease",
            YES_NO,
            format_func=yes_no_label,
            help="Does the customer have kidney disease?"
        )

        liver_disease = st.selectbox(
            "🧬 Liver Disease",
            YES_NO,
            format_func=yes_no_label,
            help="Does the customer have liver disease?"
        )

        arthritis = st.selectbox(
            "🦴 Arthritis",
            YES_NO,
            format_func=yes_no_label,
            help="Does the customer have arthritis?"
        )

        mental_health = st.selectbox(
            "🧠 Mental Health",
            YES_NO,
            format_func=yes_no_label,
            help="Does the customer have a diagnosed mental health condition?"
        )

    with col8:

        proc_imaging_count = st.number_input(
            "🩻 Imaging Procedures",
            min_value=0,
            step=1,
            format="%d",
            help="Number of imaging procedures (X-ray, MRI, etc.)."
        )

        proc_surgery_count = st.number_input(
            "🔪 Surgery Procedures",
            min_value=0,
            step=1,
            format="%d",
            help="Number of surgical procedures undergone."
        )

        proc_physio_count = st.number_input(
            "🏃 Physiotherapy Procedures",
            min_value=0,
            step=1,
            format="%d",
            help="Number of physiotherapy sessions/procedures."
        )

        proc_consult_count = st.number_input(
            "👨‍⚕️ Consultation Procedures",
            min_value=0,
            step=1,
            format="%d",
            help="Number of medical consultations."
        )

        proc_lab_count = st.number_input(
            "🧪 Lab Procedures",
            min_value=0,
            step=1,
            format="%d",
            help="Number of lab tests conducted."
        )

        is_high_risk = st.selectbox(
            "⚠️ High Risk Patient",
            YES_NO,
            format_func=yes_no_label,
            help="Is the customer classified as high risk?"
        )

        had_major_procedure = st.selectbox(
            "🏥 Major Procedure",
            YES_NO,
            format_func=yes_no_label,
            help="Has the customer had a major medical procedure?"
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