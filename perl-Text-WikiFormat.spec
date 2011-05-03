%define upstream_name    Text-WikiFormat
%define upstream_version 0.79

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Module for translating Wiki formatted text into other formats
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:  perl(URI)
BuildArch:  noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Text::WikiFormat converts text in a simple Wiki markup language to whatever
your little heart desires, provided you can describe it accurately in a
semi-regular tag language.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
