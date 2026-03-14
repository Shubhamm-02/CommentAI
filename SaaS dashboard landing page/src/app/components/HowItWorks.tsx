import { Card } from "./ui/card";
import { Instagram, Linkedin, Target, MessageSquare, BarChart3, Rocket } from "lucide-react";

const steps = [
  {
    icon: Instagram,
    number: "01",
    title: "Connect Your Accounts",
    description: "Securely link your Instagram and LinkedIn accounts in seconds. Your credentials are encrypted and protected.",
  },
  {
    icon: Target,
    number: "02",
    title: "Set Your Targets",
    description: "Define your ideal audience using hashtags, keywords, competitor profiles, or specific accounts to engage with.",
  },
  {
    icon: MessageSquare,
    number: "03",
    title: "Customize AI Voice",
    description: "Train our AI to match your unique tone and style. Set preferences for comment length, emoji use, and personality.",
  },
  {
    icon: Rocket,
    number: "04",
    title: "Let AI Engage",
    description: "Our AI automatically finds relevant posts and leaves authentic, contextual comments that drive engagement.",
  },
  {
    icon: BarChart3,
    number: "05",
    title: "Track Your Growth",
    description: "Monitor follower growth, engagement rates, and ROI with comprehensive analytics and insights.",
  },
];

export function HowItWorks() {
  return (
    <section id="how-it-works" className="py-20 px-4 sm:px-6 lg:px-8">
      <div className="container mx-auto">
        <div className="text-center max-w-3xl mx-auto mb-16">
          <h2 className="text-4xl font-bold mb-4">How CommentAI works</h2>
          <p className="text-xl text-gray-600">
            Get started in minutes and watch your social media presence grow on autopilot.
          </p>
        </div>

        <div className="max-w-5xl mx-auto">
          <div className="space-y-8">
            {steps.map((step, index) => (
              <div key={index} className="relative">
                {index < steps.length - 1 && (
                  <div className="hidden lg:block absolute left-12 top-20 bottom-0 w-0.5 bg-gradient-to-b from-purple-600 to-pink-600 opacity-20"></div>
                )}
                <Card className="p-8 hover:shadow-lg transition-shadow">
                  <div className="flex flex-col lg:flex-row gap-6 items-start">
                    <div className="flex-shrink-0">
                      <div className="w-24 h-24 bg-gradient-to-br from-purple-600 to-pink-600 rounded-2xl flex items-center justify-center relative">
                        <step.icon className="w-10 h-10 text-white" />
                        <div className="absolute -top-2 -right-2 w-8 h-8 bg-white rounded-full flex items-center justify-center shadow-lg">
                          <span className="text-sm font-bold text-purple-600">{step.number}</span>
                        </div>
                      </div>
                    </div>
                    <div className="flex-1">
                      <h3 className="text-2xl font-bold mb-3">{step.title}</h3>
                      <p className="text-gray-600 text-lg leading-relaxed">{step.description}</p>
                    </div>
                  </div>
                </Card>
              </div>
            ))}
          </div>
        </div>

        <div className="mt-16 text-center">
          <div className="inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-purple-50 to-pink-50 rounded-full">
            <Linkedin className="w-5 h-5 text-blue-600" />
            <Instagram className="w-5 h-5 text-pink-600" />
            <span className="font-semibold">Works seamlessly with Instagram & LinkedIn</span>
          </div>
        </div>
      </div>
    </section>
  );
}
