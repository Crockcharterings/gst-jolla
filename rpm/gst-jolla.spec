Name:           gstreamer0.10-jolla
Summary:        Collection of Jolla GStreamer plugins
Version:        1.0.0
Release:        1
Group:          Applications/Multimedia
License:        Proprietary
URL:            http://jollamobile.com
Source0:        gstreamer0.10-jolla-%{version}.tar.gz
BuildRequires:  pkgconfig(gstreamer-video-0.10)
Requires:       gstreamer0.10-omx
Requires:       gstreamer0.10-stecolorconv

%description
Collection of Jolla GStreamer plugins

%prep
%setup -q

%build
%autogen
%configure
make %{?jobs:-j%jobs}

%install 
%make_install

%files
%defattr(-,root,root,-)
%{_libdir}/gstreamer-0.10/libgstcodecbin.so