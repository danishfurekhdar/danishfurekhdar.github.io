source 'https://rubygems.org'

# Fix for missing timezone data on Windows
gem 'tzinfo-data', platforms: [:mingw, :mswin, :x64_mingw, :jruby]

# Optional: Improve file change detection on Windows
gem 'wdm', '>= 0.1.0' if Gem.win_platform?

group :jekyll_plugins do
  gem 'jekyll'
  gem 'jekyll-feed'
  gem 'jekyll-sitemap'
  gem 'jekyll-redirect-from'
  gem 'jemoji'
  gem 'webrick', '~> 1.8'
end

# GitHub Pages dependency (optional if you're using GitHub Pages to deploy)
gem 'github-pages'
