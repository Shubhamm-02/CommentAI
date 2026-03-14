import { Button } from "./ui/button";
import { Card } from "./ui/card";
import { Check } from "lucide-react";

const plans = [
  {
    name: "Starter",
    price: "$29",
    description: "Perfect for individuals and influencers",
    features: [
      "1 Instagram account",
      "1 LinkedIn account",
      "50 AI comments/day",
      "Basic targeting",
      "Engagement analytics",
      "Email support",
    ],
    popular: false,
  },
  {
    name: "Growth",
    price: "$79",
    description: "For professionals scaling their presence",
    features: [
      "3 Instagram accounts",
      "3 LinkedIn accounts",
      "200 AI comments/day",
      "Advanced targeting",
      "Custom AI tone & voice",
      "Detailed analytics",
      "Priority support",
      "A/B testing",
    ],
    popular: true,
  },
  {
    name: "Agency",
    price: "$199",
    description: "For agencies managing multiple clients",
    features: [
      "10 Instagram accounts",
      "10 LinkedIn accounts",
      "Unlimited AI comments",
      "Advanced AI customization",
      "White-label reports",
      "Team collaboration",
      "API access",
      "Dedicated account manager",
      "24/7 priority support",
    ],
    popular: false,
  },
];

export function Pricing() {
  return (
    <section id="pricing" className="py-20 px-4 sm:px-6 lg:px-8">
      <div className="container mx-auto">
        <div className="text-center max-w-3xl mx-auto mb-16">
          <h2 className="text-4xl font-bold mb-4">Simple, transparent pricing</h2>
          <p className="text-xl text-gray-600">
            Choose the perfect plan for your team. All plans include a 14-day free trial.
          </p>
        </div>

        <div className="grid md:grid-cols-3 gap-8 max-w-6xl mx-auto">
          {plans.map((plan, index) => (
            <Card
              key={index}
              className={`p-8 relative ${
                plan.popular ? "border-2 border-blue-600 shadow-xl" : ""
              }`}
            >
              {plan.popular && (
                <div className="absolute -top-4 left-1/2 -translate-x-1/2">
                  <span className="bg-gradient-to-r from-blue-600 to-purple-600 text-white px-4 py-1 rounded-full text-sm">
                    Most Popular
                  </span>
                </div>
              )}

              <div className="mb-6">
                <h3 className="text-2xl font-bold mb-2">{plan.name}</h3>
                <p className="text-gray-600 mb-4">{plan.description}</p>
                <div className="flex items-baseline gap-1">
                  <span className="text-4xl font-bold">{plan.price}</span>
                  <span className="text-gray-600">/month</span>
                </div>
              </div>

              <ul className="space-y-3 mb-8">
                {plan.features.map((feature, featureIndex) => (
                  <li key={featureIndex} className="flex items-start gap-2">
                    <Check className="w-5 h-5 text-green-600 shrink-0 mt-0.5" />
                    <span className="text-gray-700">{feature}</span>
                  </li>
                ))}
              </ul>

              <Button
                className="w-full"
                variant={plan.popular ? "default" : "outline"}
              >
                Start Free Trial
              </Button>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
}