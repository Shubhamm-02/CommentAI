import { Button } from "./ui/button";
import { ArrowRight } from "lucide-react";
import { ImageWithFallback } from "./figma/ImageWithFallback";

export function CTA() {
  return (
    <section className="py-20 px-4 sm:px-6 lg:px-8">
      <div className="container mx-auto">
        <div className="bg-gradient-to-br from-purple-600 to-pink-600 rounded-3xl overflow-hidden">
          <div className="grid lg:grid-cols-2 gap-8 items-center">
            <div className="p-12 text-white">
              <h2 className="text-4xl font-bold mb-4">
                Ready to 10x your social engagement?
              </h2>
              <p className="text-xl mb-8 text-purple-50">
                Join thousands of creators and businesses using CommentAI to grow their Instagram and LinkedIn presence. 
                Start your 14-day free trial today, no credit card required.
              </p>
              <div className="flex flex-col sm:flex-row gap-4">
                <Button size="lg" variant="secondary" className="text-lg px-8">
                  Start Free Trial
                  <ArrowRight className="ml-2 w-5 h-5" />
                </Button>
                <Button size="lg" variant="outline" className="text-lg px-8 bg-transparent text-white border-white hover:bg-white/10">
                  Schedule Demo
                </Button>
              </div>
            </div>

            <div className="hidden lg:block relative h-full">
              <ImageWithFallback
                src="https://images.unsplash.com/photo-1588177806780-51d021f6b2d2?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxpbnN0YWdyYW0lMjBlbmdhZ2VtZW50JTIwcGhvbmV8ZW58MXx8fHwxNzczNDkzNjkyfDA&ixlib=rb-4.1.0&q=80&w=1080&utm_source=figma&utm_medium=referral"
                alt="Instagram Engagement"
                className="w-full h-full object-cover"
              />
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}