# BMW Price Prediction: Advanced Statistical Modeling

## The Challenge
B2B auction platforms needed accurate pricing models for used BMW vehicles to optimize bidding strategies. With 4,843 BMW cars sold in 2018, the challenge was identifying which vehicle features, mileage patterns, and market timing factors most significantly impact auction prices.

## Our Solution

**Strategy:** Built and compared multiple regression approaches, ultimately developing a Ridge regression model with square-root price transformation for optimal performance.

**Key Technical Innovation:** Leveraged Ridge regression with optimized regularization (λ) to reduce overfitting, boosting predictive accuracy from 63% to 74% while maintaining actionable feature insights.

## Results That Matter
- **74% prediction accuracy** (R² = 0.74) vs 63% baseline multiple regression
- **13.8% MAPE** - industry-competitive pricing precision  
- **Key discoveries:** Mileage and engine power dominate pricing (negative and positive correlation respectively), with specific equipment features adding significant value

| Model Comparison | R² | RMSE | MAPE |
|------------------|----|----|------|
| Baseline Regression | 0.63 | 20.5 | 18.4% |
| **Ridge Regression** | **0.74** | **16.8** | **13.8%** |

![Training Curve](assets/bmw/ridge.png)

## Business Impact
This accuracy improvement enables dealers to:
- **Price inventory 26% more precisely** (13.6% vs 18.4% error rate)
- Reduce time-to-sale through optimized market positioning
- Increase profit margins with data-driven pricing strategies

## Technical Implementation
- **Tools:** R (glmnet, caret, ggplot2), cross-validation, statistical modeling
- **Data:** 4,843 auction records, 15+ vehicle features
- **Scale:** Comprehensive analysis across fuel types, car categories, and equipment packages

### Model Validation
![True vs Predicted](assets/bmw/prediction.png)
![Residuals Analysis](assets/bmw/residual.png)

**[View Full Analysis & Code →](assets/bmw/Final_Report_C2G3.pdf)**