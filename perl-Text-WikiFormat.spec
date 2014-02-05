%define upstream_name    Text-WikiFormat
%define upstream_version 0.81

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Module for translating Wiki formatted text into other formats
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Text/Text-WikiFormat-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(URI)
BuildArch:	noarch

%description
Text::WikiFormat converts text in a simple Wiki markup language to whatever
your little heart desires, provided you can describe it accurately in a
semi-regular tag language.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Text
%{_mandir}/man3/*

%changelog
* Tue May 03 2011 Michael Scherer <misc@mandriva.org> 0.790.0-2mdv2011.0
+ Revision: 664898
- mass rebuild

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.790.0-1mdv2010.0
+ Revision: 406193
- rebuild using %%perl_convert_version

* Thu Jul 10 2008 Michael Scherer <misc@mandriva.org> 0.79-2mdv2009.0
+ Revision: 233583
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Jul 01 2007 Michael Scherer <misc@mandriva.org> 0.79-1mdv2008.0
+ Revision: 46490
- 0.79

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 0.78-2mdv2008.0
+ Revision: 23638
- rebuild


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.78-2mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Source URL

* Sat Apr 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.78-1mdk
- New release 0.78

* Mon Nov 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.77-1mdk
- New release 0.77
- spec cleanup
- don't ship empty directories
- don't need to remove signature check

* Fri Nov 04 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.76-2mdk
- Fix BuildRequires

* Sat Oct 01 2005 misc@mandriva.org 0.76-1mdk
- First mandriva package



