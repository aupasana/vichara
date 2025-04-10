init:
	source /opt/homebrew/opt/chruby/share/chruby/chruby.sh && chruby ruby-3.4.1 && bundle install

serve: 
	source /opt/homebrew/opt/chruby/share/chruby/chruby.sh && chruby ruby-3.4.1 && bundle exec jekyll serve

work_to_main:
	git checkout main
	git reset --hard work
	git reset $(git commit-tree "HEAD^{tree}" -m "initialize")

main_to_work:
	git checkout work
	git checkout main -- .
	