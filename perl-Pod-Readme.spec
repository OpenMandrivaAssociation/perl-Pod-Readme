%define upstream_name    Pod-Readme
%define upstream_version 0.10

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Convert Module POD to a README file
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Pod/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(File::Copy)
BuildRequires: perl(IO::File)
BuildRequires: perl(Pod::Text)
BuildRequires: perl(Regexp::Common)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module is a subclass of L<Pod::PlainText> which provides additional
POD markup for generating F<README> files.

Why should one bother with this? One can simply use

  pod2text Module.pm > README

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README META.yml Changes
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%perl_vendorlib/*


