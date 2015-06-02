#ifndef ProducePFCalibrationObject_H
#define ProducePFCalibrationObject_H

/** \class ProducePFCalibrationObject
 *  No description available.
 *
 *  \author G. Cerminara - CERN
 */
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "TFile.h"
#include "TGraph.h"

#include <vector>
#include <string>

class ProducePFCalibrationObject  : public edm::EDAnalyzer {
public:
  /// Constructor
  ProducePFCalibrationObject(const edm::ParameterSet&);

  /// Destructor
  virtual ~ProducePFCalibrationObject();

  // Operations
//   virtual void beginJob();
  virtual void beginRun(const edm::Run& run, const edm::EventSetup& eSetup);
  
  virtual void analyze(const edm::Event&, const edm::EventSetup&) {}
  virtual void endJob() {}

  void Book();

protected:

private:

  bool read;
  bool write;

  std::vector<edm::ParameterSet> fToWrite;
  std::vector<std::string> fToRead;

  std::string outputfile_; 
  TFile *fout;

  static const int n_func = 10;

  TGraph *gcalib_func[n_func]; 

};
#endif

