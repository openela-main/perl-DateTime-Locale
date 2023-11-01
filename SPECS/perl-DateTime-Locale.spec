Name:           perl-DateTime-Locale
Version:        1.17
Release:        2%{?dist}
Summary:        Localization support for DateTime.pm
# Although the CLDR license is listed as "MIT" on the Fedora Wiki, it's more
# similar to recently added "Unicode" license.
# some modules under DateTime/Locale:   Unicode (generated from data
#                                       provided by the CLDR project)
# LICENSE.cldr:         Unicode
# other files:          GPL+ or Artistic
License:        (GPL+ or Artistic) and Unicode
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/DateTime-Locale/
Source0:        http://www.cpan.org/authors/id/D/DR/DROLSKY/DateTime-Locale-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::ShareDir::Install) >= 0.06
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
# Dist::CheckConflicts 0.02 is optionaly used from Makefile.PL, but it has no
# meaning in minimal build root without useless Perl modules.
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(namespace::autoclean) >= 0.19
BuildRequires:  perl(Params::ValidationCompiler) >= 0.13
BuildRequires:  perl(Specio::Declare)
BuildRequires:  perl(Specio::Library::String)
# Tests only
BuildRequires:  perl(base)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::File::ShareDir::Dist)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(utf8)
# Optional tests:
BuildRequires:  perl(CPAN::Meta) >= 2.120900
BuildRequires:  perl(CPAN::Meta::Check) >= 0.011
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Storable)
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))
Requires:       perl(Dist::CheckConflicts) >= 0.02
# perl-DateTime-Locale used to be bundled with perl-DateTime
# ideally, this would be resolved with
# Requires:     perl-DateTime >= 2:0.70-1
# but DateTime::Locale doesn't strictly require DateTime
# and this would introduce circular build dependencies
Conflicts:      perl-DateTime <= 1:0.7000-3.fc16

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Dist::CheckConflicts\\)$

%description
DateTime::Locale is primarily a factory for the various locale sub-classes.
It also provides some functions for getting information on all the
available locales.

%prep
%setup -q -n DateTime-Locale-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE LICENSE.cldr
%doc Changes CONTRIBUTING.md README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.17-1
- 1.17 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.16-2
- Perl 5.26 rebuild

* Wed Mar 22 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.16-1
- 1.16 bump

* Mon Mar 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.14-1
- 1.14 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 30 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.12-1
- 1.12 bump

* Mon Nov 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.11-1
- 1.11 bump

* Mon Oct 24 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.10-1
- 1.10 bump

* Tue Oct 11 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-1
- 1.09 bump

* Tue Sep 27 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.08-1
- 1.08 bump

* Mon Sep 19 2016 Petr Pisar <ppisar@redhat.com> - 1.05-3
- Correct license to ((GPL+ or Artistic) and Unicode)

* Wed Jul 13 2016 Petr Pisar <ppisar@redhat.com> - 1.05-2
- Simplify optional build-time dependencies

* Mon Jun 27 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.05-1
- 1.05 bump

* Mon Jun 20 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.04-1
- 1.04 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-2
- Perl 5.24 rebuild

* Tue Mar 29 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-1
- 1.03 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 11 2015 Petr Šabata <contyk@redhat.com> - 1.02-1
- 1.02 bump

* Tue Nov 10 2015 Petr Šabata <contyk@redhat.com> - 1.01-1
- 1.01 bump, lots of backwards incompatible changes

* Tue Sep 29 2015 Petr Šabata <contyk@redhat.com> - 0.92-1
- 0.92 bump, no changes (yet)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.46-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.46-2
- Perl 5.22 rebuild

* Wed May 27 2015 Petr Šabata <contyk@redhat.com> - 0.46-1
- 0.46 bump

* Tue Jan 13 2015 Petr Pisar <ppisar@redhat.com> - 0.45-11
- Modernize spec file

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.45-10
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.45-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.45-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 26 2013 Petr Pisar <ppisar@redhat.com> - 0.45-7
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.45-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 13 2012 Marcela Mašláňová <mmaslano@redhat.com> - 0.45-5
- Add BR, fix whitespaces

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.45-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Petr Pisar <ppisar@redhat.com> - 0.45-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 15 2011 Iain Arnell <iarnell@gmail.com> 0.45-1
- Specfile autogenerated by cpanspec 1.78.
