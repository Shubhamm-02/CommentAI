import { BarChart3, Zap, Shield, Users, Globe, Sparkles } from "lucide-react";
import { Card } from "./ui/card";

const features = [
  {
    icon: Sparkles,
    title: "AI-Powered Comments",
    description: "Generate authentic, context-aware comments that match your brand voice and engage naturally with your audience.",
  },
  {
    icon: Zap,
    title: "Auto-Engagement",
    description: "Automatically comment on relevant posts in your niche on Instagram and LinkedIn to boost your visibility.",
  },
  {
    icon: BarChart3,
    title: "Engagement Analytics",
    description: "Track your growth, engagement rates, and ROI with detailed analytics and performance insights.",
  },
  {
    icon: Users,
    title: "Targeted Audience",
    description: "Use AI to identify and engage with posts from your ideal audience using hashtags, keywords, and profiles.",
  },
  {
    icon: Shield,
    title: "Safe & Compliant",
    description: "Stay within platform limits with smart rate limiting and human-like behavior patterns to avoid detection.",
  },
  {
    icon: Globe,
    title: "Multi-Account Support",
    description: "Manage multiple Instagram and LinkedIn accounts from one dashboard with separate strategies for each.",
  },
];

export function Features() {
  return (
    <section id="features" className="py-20 px-4 sm:px-6 lg:px-8 bg-gray-50">
      <div className="container mx-auto">
        <div className="text-center max-w-3xl mx-auto mb-16">
          <h2 className="text-4xl font-bold mb-4">Everything you need to grow</h2>
          <p className="text-xl text-gray-600">
            Powerful AI features designed to help you build authentic relationships and grow your social media presence effortlessly.
          </p>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {features.map((feature, index) => (
            <Card key={index} className="p-6 hover:shadow-lg transition-shadow">
              <div className="w-12 h-12 bg-gradient-to-br from-blue-600 to-purple-600 rounded-lg flex items-center justify-center mb-4">
                <feature.icon className="w-6 h-6 text-white" />
              </div>
              <h3 className="text-xl font-semibold mb-2">{feature.title}</h3>
              <p className="text-gray-600">{feature.description}</p>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
}