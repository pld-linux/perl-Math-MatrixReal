%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	MatrixReal
Summary:	Math::MatrixReal perl module
Summary(pl):	Modu� perla Math::MatrixReal
Name:		perl-Math-MatrixReal
Version:	1.9
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::MatrixReal perl module.

%description -l pl
Modu� perla Math::MatrixReal.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/Math/*
%{_mandir}/man3/*
