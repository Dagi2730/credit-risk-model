# credit-risk-model

📘 Credit Scoring Business Understanding
1. How does the Basel II Accord’s emphasis on risk measurement influence our need for an interpretable and well-documented model?
The Basel II Capital Accord provides a regulatory framework that requires banks to quantify, manage, and report credit risk more effectively. It allows institutions to develop their own Internal Ratings-Based (IRB) models for credit assessment, but these must adhere to strict standards of transparency, validation, and accountability.

This creates a strong demand for credit risk models that are:

Interpretable: The logic behind each prediction must be clearly understandable by analysts and regulators.

Well-documented: Every transformation, assumption, and decision in the modeling process must be recorded and justified.

Auditable: Models must be reproducible and their outcomes explainable to external auditors and internal risk teams.

In practical terms, this means prioritizing models that are not black boxes. Tools like Weight of Evidence (WoE) and Logistic Regression are favored because they translate inputs into understandable effects on risk, aligning closely with Basel II’s goals of risk transparency and responsible governance.

2. Since we lack a direct "default" label, why is creating a proxy variable necessary, and what are the potential business risks of making predictions based on this proxy?
In our dataset, there is no explicit indicator that tells us whether a customer defaulted on a loan. However, to train a supervised machine learning model, a target label is required. Therefore, we must create a proxy variable—an indirect indicator that approximates the concept of "default."

One widely accepted method is to engineer a proxy using RFM analysis (Recency, Frequency, and Monetary value). By evaluating how recently a customer made a transaction, how often they transact, and how much they spend, we can infer behavioral signals of risk. For example:

Customers with low frequency and low transaction amounts over long periods may be flagged as disengaged or high-risk.

However, using a proxy comes with significant business risks:

Labeling errors: A poorly defined proxy may misclassify reliable customers as risky (or vice versa), leading to poor credit decisions.

Model mislearning: The model may learn patterns that reflect noise in the proxy rather than true risk behavior.

Regulatory scrutiny: Predicting creditworthiness from an unvalidated proxy may be challenged by regulators or risk departments.

To mitigate these risks, proxy construction must be methodologically sound, explainable, and validated with business logic.

3. What are the key trade-offs between using a simple, interpretable model (like Logistic Regression with WoE) versus a complex, high-performance model (like Gradient Boosting) in a regulated financial context?
In credit scoring—especially under the scrutiny of financial regulators—there is a fundamental trade-off between performance and interpretability.

Factor	Simple Model (e.g., Logistic Regression + WoE)	Complex Model (e.g., Gradient Boosting / XGBoost)
Interpretability	High – easily explainable to stakeholders	Low – requires tools like SHAP or LIME
Regulatory Approval	Easy to audit and justify	More difficult to explain model behavior
Bias Detection	Easier to detect and correct	Complex interactions can hide biases
Performance	May underfit non-linear or complex relationships	High accuracy, can capture subtle patterns
Ease of Deployment	Lightweight, easy to monitor	Requires robust infrastructure and explainability layers

In regulated environments such as banking, simplicity and interpretability are often prioritized. However, if a complex model offers significantly better performance, it may still be adopted provided it is:

Accompanied by explainability frameworks (e.g., SHAP values)

Thoroughly tested and validated

Supported with strong documentation and governance processes

Ultimately, model choice must align with both regulatory standards and business objectives.

✅ Summary
This section ensures we have a solid foundation for our credit scoring model by:

Aligning with regulatory expectations (Basel II)

Justifying the use of a proxy target

Evaluating the trade-offs between interpretability and performance

This foundation will guide all further work, including feature engineering, proxy construction, model training, and deployment.
