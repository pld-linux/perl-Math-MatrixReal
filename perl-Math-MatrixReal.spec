%define	pdir	Math
%define	pnam	MatrixReal
%include	/usr/lib/rpm/macros.perl
Summary:	Math-MatrixReal perl module
Summary(pl):	Modu³ perla Math-MatrixReal
Name:		perl-Math-MatrixReal
Version:	1.3a5
Release:	5

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math-MatrixReal perl module.

%description -l pl
Modu³ perla Math-MatrixReal.

%prep
%setup -q -n Math-MatrixReal-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Math/MatrixReal.pm
%{_mandir}/man3/*
