init:
	source /opt/homebrew/opt/chruby/share/chruby/chruby.sh && chruby ruby-3.4.1 && bundle install

serve: 
	source /opt/homebrew/opt/chruby/share/chruby/chruby.sh && chruby ruby-3.4.1 && bundle exec jekyll serve

# Export snippet cards to images. `make snippets` does all of them,
# `make snippets snip_vs_0001` (or SNIPPET=snip_vs_0001) just that one.
# A bare name arrives as a second goal rather than a variable, so lift it out
# of MAKECMDGOALS and give it a do-nothing rule so make stops looking for one.
ifneq ($(filter snippets,$(MAKECMDGOALS)),)
SNIPPET ?= $(filter-out snippets,$(MAKECMDGOALS))
ifneq ($(SNIPPET),)
$(eval $(SNIPPET):;@:)
endif
endif

snippets:
# 	source /opt/homebrew/opt/chruby/share/chruby/chruby.sh && chruby ruby-3.4.1 && bundle exec jekyll build
	path/to/venv/bin/python scripts/snippet_export.py $(SNIPPET)
	open $(if $(SNIPPET),$(addprefix exports/snippets/,$(addsuffix .png,$(SNIPPET))),exports/snippets)

work_to_main:
	git checkout main
	git reset --hard work
	git reset $(git commit-tree "HEAD^{tree}" -m "initialize")

main_to_work:
	git checkout work
	git checkout main -- .
	