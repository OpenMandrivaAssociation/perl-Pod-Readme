%define upstream_name    Pod-Readme
%define upstream_version v1.2.3

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	Convert Module POD to a README file
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/bigpresh/Pod-Readme
Source0:	https://cpan.metacpan.org/authors/id/R/RR/RRWO/Pod-Readme-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(Pod::Text)
BuildRequires:	perl(Regexp::Common)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)

BuildArch:	noarch

%description
This module is a subclass of L<Pod::PlainText> which provides additional
POD markup for generating F<README> files.

Why should one bother with this? One can simply use

  pod2text Module.pm > README

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README META.yml Changes
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.110.0-2mdv2011.0
+ Revision: 657828
- rebuild for updated spec-helper

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 0.11

* Wed Aug 25 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2011.0
+ Revision: 573147
- import perl-Pod-Readme

