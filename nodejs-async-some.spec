%{?scl:%scl_package nodejs-async-some}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-async-some

%global npm_name async-some
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-async-some
Version:	1.0.2
Release:	3%{?dist}
Summary:	Short-circuited, asynchronous version of Array.prototype.some
Url:		https://github.com/othiym23/async-some
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	ISC

BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

BuildRequires:	%{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(dezalgo)
BuildRequires:	%{?scl_prefix}npm(tap)
%endif

%description
Short-circuited, asynchronous version of Array.prototype.some

%prep
%setup -q -n package

#%{nodejs_fixdep} tap

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json some.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check
tap test/*.js
%endif

%files
%{nodejs_sitelib}/async-some

%doc README.md
%doc LICENSE

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.2-3
- rebuilt

* Fri Nov 27 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.2-2
- Enable scl macros

* Wed Jun 24 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.2-1
- Updated to new upstream release

* Wed May 13 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.1-1
- Initial build
