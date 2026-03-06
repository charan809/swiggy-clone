import React, { useState } from 'react';
import { Routes, Route } from 'react-router-dom';

import './index.css';
import Header from './components/Header';
import Footer from './components/Footer';
import ContactUs from './components/ContactUs';
import Login from './components/Login';
import Instamart from './components/Instamart';
import ContactForm from './components/ContactForm';
import SidePanelModal from './components/SidePanelModal';
import BlogSection from './components/BlogSection';
import Collection from './components/Collection';
import PartnerWithUs from './components/PartnerWithUs';
import 'bootstrap/dist/css/bootstrap.min.css';
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

// Import Home Page Sections
import MainSection1 from './components/MainSection1';
import MainSection2 from './components/MainSection2';
import MainSection3 from './components/MainSection3';
import MainSection4 from './components/MainSection4';
import MainSection5 from './components/MainSection5';
import BestPlacesSection from './components/BestPlacesSection';
import BestGrocery from './components/BestGrocery';

function HomePage() {
  return (
    <>
      <MainSection1 />
      <MainSection2 />
      <MainSection3 />
      <MainSection4 />
      <MainSection5 />
      <BestPlacesSection />
      <BestGrocery />
    </>
  );
}

function App() {
  const [isSidebarOpen, setSidebarOpen] = useState(false);

  const toggleSidebar = () => {
    setSidebarOpen(!isSidebarOpen);
  };

  return (
    <div className="App">
      {/* Header */}
      <Header toggleSidebar={toggleSidebar} />

      <ToastContainer />

      {/* Sidebar Modal */}
      <SidePanelModal isOpen={isSidebarOpen} toggleSidebar={toggleSidebar} />

      {/* Routes */}
      <Routes className="pt-18 pb-18">
        <Route path="/" element={<HomePage />} />
        <Route path="/contact" element={<ContactUs />} />
        <Route path="/contact-form" element={<ContactForm />} />
        <Route path="/login" element={<Login />} />
        <Route path="/partnerWithUs" element={<PartnerWithUs />} />
        <Route path="/instamart" element={<Instamart />} />
        <Route path="/blogSection" element={<BlogSection />} />
        <Route path="/collection" element={<Collection />} />
      </Routes>

      {/* Footer and Navbar should be outside Routes to appear on every page */}
      <Footer />
    </div>
  );
}

export default App;
