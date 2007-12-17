%define module   Text-WikiFormat
%define name	perl-%{module}
%define version 0.79

Name: 		%{name}
Version: 	%{version}
Release:        %mkrel 1
Summary:	Module for translating Wiki formatted text into other formats
License:	GPL or Artistic
Group:		Development/Perl
Source0:        ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:  perl(URI)
BuildArch:      noarch

%description
Text::WikiFormat converts text in a simple Wiki markup language to whatever
your little heart desires, provided you can describe it accurately in a
semi-regular tag language.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Text
%{_mandir}/man3/*

