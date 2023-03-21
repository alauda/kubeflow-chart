TOPDIR=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

update_chart_dependencies_version:
	$(TOPDIR)/script/update_chart_dependencies_version.sh
